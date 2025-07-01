
import pandas as pd
import os


def generar_tablahechos(numero):
    print("=========== generar  datos================")

    # Leer el archivo de origen
    nombre_archivo_origen = "archivos_csv/dataset_"+str(numero)+".csv"
    df_origen = pd.read_csv(nombre_archivo_origen)

    # Crear diccionarios para almacenar IDs únicos por dimensión
    dimensiones = {}


    dimensiones_nombres = [
        "County", "City", "State", "Postal Code", "Model Year", "Make", 
        "Model", "Electric Vehicle Type", "Clean Alternative Fuel Vehicle (CAFV) Eligibility", "Electric Range", "Base MSRP", "Legislative District", "Vehicle Location", "Electric Utility"
    ]

    # Asignar IDs únicos a cada valor de las dimensiones y crear DataFrames de dimensiones
    for col in dimensiones_nombres:
        valores_unicos = df_origen[col].dropna().unique()
        dimensiones[col] = {valor: idx + 1 for idx, valor in enumerate(valores_unicos)}

    # Crear listas para las tablas de dimensiones
    tablas_dimensiones = {}
    for col in dimensiones_nombres:
        tablas_dimensiones[col] = pd.DataFrame(
            list(dimensiones[col].items()), columns=[ col,f"ID_{col}"]
        )

    # Crear la tabla de hechos con los IDs
    registros = []
    for _, row in df_origen.iterrows():
        registros.append([
            row["VIN (1-10)"],
            dimensiones["County"].get(row["County"], None), row["County"],
            dimensiones["City"].get(row["City"], None), row["City"],
            dimensiones["State"].get(row["State"], None), row["State"],
            dimensiones["Postal Code"].get(row["Postal Code"], None), row["Postal Code"],
            dimensiones["Model Year"].get(row["Model Year"], None), row["Model Year"],
            dimensiones["Make"].get(row["Make"], None), row["Make"],
            dimensiones["Model"].get(row["Model"], None), row["Model"],
            dimensiones["Electric Vehicle Type"].get(row["Electric Vehicle Type"], None), row["Electric Vehicle Type"],
            dimensiones["Clean Alternative Fuel Vehicle (CAFV) Eligibility"].get(row["Clean Alternative Fuel Vehicle (CAFV) Eligibility"], None), 
            row["Clean Alternative Fuel Vehicle (CAFV) Eligibility"],
            dimensiones["Base MSRP"].get(row["Base MSRP"], None), row["Base MSRP"],
            dimensiones["Electric Range"].get(row["Electric Range"], None), row["Electric Range"],
            dimensiones["Legislative District"].get(row["Legislative District"], None), row["Legislative District"],row["DOL Vehicle ID"],
            dimensiones["Vehicle Location"].get(row["Vehicle Location"], None), row["Vehicle Location"],
            dimensiones["Electric Utility"].get(row["Electric Utility"], None), row["Electric Utility"],row['2020 Census Tract']
                        




            
        ])

    # Crear DataFrame con la tabla de hechos
    df_hechos = pd.DataFrame(registros, columns=[
        "VIN (1-10)", 
        "ID_County", "County",
        "ID_City", "City",
        "ID_State", "State",
        "ID_Postal_Code", "Postal Code",
        "ID_Model_Year", "Model Year",
        "ID_Make", "Make",
        "ID_Model", "Model",
        "ID_Electric_Vehicle_Type", "Electric Vehicle Type",
        "ID_Clean_Alternative_", "(CAFV) ",
        "ID_Base_MSRP", "Base MSRP",
        "ID_Electric_Range", "Electric Range",
        "ID_Legislative_District", "Legislative District",
        "DOL Vehicle ID",
        "ID_Vehicle_Location", "Vehicle Location",
       
        "ID_Electric_Utility", "Electric Utility" , "2020 Census Tract"
    ])

    # creo la carpeta 
    if not os.path.exists("modelo_de_datos_(tablas_de_hechos)"):
        os.makedirs("modelo_de_datos_(tablas_de_hechos)")


    # Guardar en un archivo Excel con varias hojas
    nombre_archivo_destino = "modelo_de_datos_(tablas_de_hechos)/modelo_datos_"+str(numero)+".xlsx"
    with pd.ExcelWriter(nombre_archivo_destino, engine="openpyxl") as writer:
        df_hechos.to_excel(writer, sheet_name="Tabla_Hechos", index=False)
        for col, df_dim in tablas_dimensiones.items():
            df_dim.to_excel(writer, sheet_name=f"Dim_{col}", index=False)

    print(f"Modelo de datos generado en: {nombre_archivo_destino}")

# usar bucle 

contador = 1
limite = 5
while(contador < limite ):
    
    generar_tablahechos(contador)

    contador = contador + 1
