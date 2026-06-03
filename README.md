# Visualización de Grandes Volúmenes de Datos con Apache Spark

**Asignatura:** Herramientas y Visualización de Datos  
**Estudiante:** Jhon Alexander Vargas Catuche  
**Dataset:** NYC Yellow Taxi Trip Records  
**Fuente:** [NYC Taxi & Limousine Commission (TLC)](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)  
**Período analizado:** 2023 – 2024

---

## Descripción

Este proyecto desarrolla un análisis exploratorio y visual de más de **79 millones de registros** de viajes en taxis amarillos de Nueva York, utilizando **Apache Spark** para el procesamiento distribuido y **Matplotlib / Seaborn** para la visualización.

El flujo completo incluye descarga automática de datos, limpieza, transformación de variables temporales y la generación de 5 visualizaciones con sus respectivas interpretaciones.

---

## Preguntas de Análisis

| # | Pregunta |
|---|---|
| 1 | ¿Cómo evoluciona la cantidad de viajes por mes en 2023 y 2024? |
| 2 | ¿Cuáles son los medios de pago más utilizados por los pasajeros? |
| 3 | ¿Qué relación existe entre la distancia del viaje y el valor total pagado? |
| 4 | ¿En qué días y horas se concentra la mayor demanda de taxis? |
| 5 | ¿Cómo se distribuyen los valores pagados por los usuarios? |

---

## Visualizaciones Generadas

| Archivo | Descripción |
|---|---|
| `outputs/visualizacion_1_evolucion_mensual.png` | Evolución mensual de viajes (2023 vs 2024) |
| `outputs/visualizacion_2_medios_pago.png` | Medios de pago más utilizados |
| `outputs/visualizacion_3_distancia_total.png` | Dispersión distancia vs valor total pagado |
| `outputs/visualizacion_4_calor_dia_hora.png` | Mapa de calor: demanda por día y hora |
| `outputs/visualizacion_5_distribucion_total.png` | Distribución del valor total pagado |

---

## Estructura del Proyecto

```text
hvd_spark_final/
│
├── Vargas_Catuche_HVD_Spark.ipynb      ← Notebook principal
├── README.md                           ← Este archivo
├── requirements.txt                    ← Dependencias con versiones fijas
├── test_parquet.py                     ← Script auxiliar de prueba de lectura
├── .gitignore                          ← Exclusiones de Git
│
├── data/                               ← Archivos Parquet (NO se suben a GitHub)
└── outputs/                            ← Gráficas exportadas (.png)
```

---

## Requisitos del Sistema

| Requisito | Mínimo recomendado |
|---|---|
| Python | 3.9 o superior |
| RAM disponible | 8 GB |
| Espacio en disco | 5 GB libres (para los Parquet) |
| Java (JDK) | 8 u 11 — **requerido por Spark** |

> **Windows:** Descarga Java desde [adoptium.net](https://adoptium.net/) e instálalo antes de continuar.  
> **macOS / Linux:** Verifica con `java -version`. Si no está instalado: `brew install openjdk@11` (macOS) o `sudo apt install openjdk-11-jdk` (Ubuntu).

---

## Instalación

```bash
# 1. Clonar el repositorio
git clone <url-del-repositorio>
cd hvd_spark_final

# 2. (Opcional) Crear y activar un entorno virtual
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows

# 3. Instalar dependencias
pip install -r requirements.txt
```

---

## Ejecución

1. Abre el notebook `Vargas_Catuche_HVD_Spark.ipynb` en Jupyter o VS Code.
2. Ejecuta las celdas en orden, desde la primera.
3. La celda de descarga obtendrá automáticamente los archivos Parquet de la NYC TLC.
4. Verifica que el tamaño total de `data/` supere **1 GB** antes de continuar.
5. Ejecuta el resto de las celdas hasta completar las 5 visualizaciones.
6. Guarda el notebook con las salidas visibles antes de entregar.

> **Consejo para equipos lentos:** Cambia temporalmente `YEARS = [2024]` y `MONTHS = range(1, 4)` para probar el flujo con menos datos antes de descargar todo.

---

## Dataset

| Campo | Detalle |
|---|---|
| **Nombre** | NYC Yellow Taxi Trip Records |
| **Fuente** | NYC Taxi & Limousine Commission |
| **Formato** | Parquet (un archivo por mes) |
| **URL base** | `https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_YYYY-MM.parquet` |
| **Período** | Enero 2023 – Diciembre 2024 (24 archivos) |
| **Tamaño total** | > 1 GB |

---

## Notas Importantes

- La carpeta `data/` **no se sube a GitHub** porque los archivos Parquet son demasiado grandes.  
  El notebook descarga los datos automáticamente al ejecutarse.
- La carpeta `outputs/` contiene las gráficas ya generadas y **sí se incluye** en el repositorio.
- Si Spark lanza advertencias de `HADOOP_HOME`, puedes ignorarlas en Windows; no afectan la ejecución.
