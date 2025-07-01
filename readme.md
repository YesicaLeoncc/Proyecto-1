# 🧠 Generación de Tabla de Hechos con Python

Este proyecto tiene como objetivo la construcción automatizada de una **tabla de hechos** (fact table), diseñada para análisis de datos y modelado dimensional, a partir de múltiples fuentes de datos heterogéneas . Utiliza procesamiento y transformación de datos en Python, asegurando limpieza, consistencia y escalabilidad.
se ha usado   conjunto de  Datos de población de vehículos eléctricos :  vehículos eléctricos de batería (BEV) y los vehículos eléctricos híbridos enchufables (PHEV) que actualmente están registrados a través del Departamento de Licencias del Estado de Washington (DOL).






![image](https://github.com/user-attachments/assets/473f08e7-2210-4f4c-9cfb-fb194cf76b78)





## ⚙️ ¿Qué es una Tabla de Hechos?

Una **tabla de hechos** almacena métricas cuantitativas que se pueden analizar, como ventas, ingresos, clics, etc. Se conecta con múltiples tablas de dimensiones para permitir análisis multidimensionales en soluciones de inteligencia de negocio.

---

## 🔗 Fuentes de Datos Utilizadas

- 🧾 Archivos  (CSV)
- 🛠️ Bases de datos relacionales 
- ☁️  fuentes en la nube (https://catalog.data.gov/dataset/electric-vehicle-population-data) 


Cada una de estas fuentes pasa por un proceso de transformación que las normaliza y estandariza para su integración.

---

## 🐍 Procesamiento en Python

Se emplean librerías de ciencia de datos como:

- `pandas` – para carga, limpieza y transformación de datos
- `sqlalchemy` / `pyodbc` – para conexión a bases de datos
- `openpyxl` / `xlrd` – para manejar archivos Excel


### 🔄 Proceso ETL Simplificado

1. **Extracción (E):**
   - Se cargan datos desde múltiples orígenes (OECD Data explorer)
  

2. **Transformación (T):**
   
   - Se genera una estructura común y cohesiva.

3. **Carga (L):**
   - La tabla de hechos se genera en un formato final (CSV).
   

---



