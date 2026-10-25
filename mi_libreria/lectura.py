import pandas as pd

def leer_csv(ruta):
    # Esta función lee un archivo csv a través de la ruta proporcionada como argumento.
    try:
        # Los bloques try/except permiten manejar los posibles errores.
        return pd.read_csv(ruta)
    except FileNotFoundError:
        print("ERROR: El archivo CSV no existe o no se ha encontrado.")
    except pd.errors.EmptyDataError:
        print("Error: El archivo de ventas está vacío.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

def leer_parquet(ruta):
    # Esta función lee un archivo parquet a través de la ruta proporcionada como argumento.
    try:
        return pd.read_parquet(ruta)
    except FileNotFoundError:
        print("ERROR: El archivo Parquet no existe o no se ha encontrado.")
    except pd.errors.EmptyDataError:
        print("Error: El archivo de ventas está vacío.")
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
