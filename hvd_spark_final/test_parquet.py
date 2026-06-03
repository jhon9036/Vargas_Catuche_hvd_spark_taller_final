import os
import sys
import warnings
from pathlib import Path

import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

warnings.filterwarnings('ignore')

# ── Rutas del proyecto ──────────────────────────────────────────────────
PROJECT_DIR = Path(__file__).parent.resolve()
DATA_DIR    = PROJECT_DIR / 'data'
OUTPUT_DIR  = PROJECT_DIR / 'outputs'

print(f'Carpeta del proyecto : {PROJECT_DIR}')
print(f'Carpeta de datos     : {DATA_DIR}')

# ── Variables de entorno para PySpark ───────────────────────────────────
os.environ.setdefault('PYSPARK_PYTHON', sys.executable)
os.environ.setdefault('PYSPARK_DRIVER_PYTHON', sys.executable)

# Configuracion adicional necesaria en Windows
if sys.platform.startswith('win'):
    import tempfile
    import urllib.request
    hadoop_home = Path(tempfile.gettempdir()) / 'hadoop'
    (hadoop_home / 'bin').mkdir(parents=True, exist_ok=True)
    os.environ.setdefault('HADOOP_HOME', str(hadoop_home))
    os.environ.setdefault('hadoop.home.dir', str(hadoop_home))

    winutils_path = hadoop_home / 'bin' / 'winutils.exe'
    if not winutils_path.exists():
        winutils_url = (
            'https://github.com/cdarlint/winutils/raw/master/'
            'hadoop-3.3.5/bin/winutils.exe'
        )
        try:
            print('Descargando winutils.exe para Windows...', end=' ')
            urllib.request.urlretrieve(winutils_url, winutils_path)
            print('OK')
        except Exception as e:
            print('ADVERTENCIA: {}'.format(e))

# ── Crear sesion Spark ──────────────────────────────────────────────────
try:
    spark.stop()
except:
    pass

spark = (
    SparkSession.builder
    .master('local[*]')
    .appName('HVD_Spark_NYC_Taxi')
    .config('spark.driver.memory', '6g')
    .config('spark.sql.shuffle.partitions', '8')
    .config('spark.sql.adaptive.enabled', 'true')
    .config('spark.sql.files.ignoreCorruptFiles', 'false')
    .getOrCreate()
)

spark.sparkContext.setLogLevel('ERROR')
print('[OK] Sesion Spark iniciada (version {})\n'.format(spark.version))

# ── CELDA 11: Listar archivos ───────────────────────────────────────────
print('=' * 70)
print('CELDA 11: Listando archivos parquet')
print('=' * 70)

parquet_files = sorted(DATA_DIR.glob('*.parquet'))
total_size_gb = sum(f.stat().st_size for f in parquet_files) / (1024 ** 3)

# CORRECCION: Forward slashes sin file:// protocol
if sys.platform.startswith('win'):
    parquet_paths = [str(f.resolve()).replace('\\', '/') for f in parquet_files]
else:
    parquet_paths = [str(f.resolve()) for f in parquet_files]

print('Archivos Parquet encontrados : {}'.format(len(parquet_files)))
print('Tamaño total                : {:.2f} GB\n'.format(total_size_gb))
print('Primeros 10 archivos:')
for f in parquet_files[:10]:
    print('  {:45s} {:>7.1f} MB'.format(f.name, f.stat().st_size / (1024**2)))

if not parquet_paths:
    raise FileNotFoundError('No se encontraron archivos .parquet en {}'.format(DATA_DIR))

print('\n[OK] Total de rutas generadas: {}'.format(len(parquet_paths)))

# ── CELDA 13: Prueba de lectura ─────────────────────────────────────────
print('\n' + '=' * 70)
print('CELDA 13: Prueba de lectura del primer archivo')
print('=' * 70 + '\n')

archivo_prueba = parquet_paths[0]
print('Archivo de prueba:')
print(archivo_prueba)
print()

try:
    df_prueba = spark.read.parquet(archivo_prueba)
    print('[OK] Lectura exitosa.\n')
    print('Schema:')
    df_prueba.printSchema()
    print('\nPrimeras 3 filas:')
    df_prueba.show(3, truncate=False)
    print('\n[OK] PRUEBA COMPLETADA SIN ERRORES')
except Exception as e:
    print('[ERROR] {}'.format(e))
    import traceback
    traceback.print_exc()

spark.stop()
print('\n[OK] Sesion Spark cerrada.')
