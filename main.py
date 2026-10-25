from pathlib import Path
from mi_libreria.lectura import leer_csv, leer_parquet
from mi_libreria.calculos import calculo_importe, ventas_totalesYcategorias

carpeta = Path(__file__).parent / "datos"
Nombre_CSV = input("\nIntroduce el nombre del archivo CSV con el que desea trabajar (Incluyendo la extensión):")
try:
    ventas = leer_csv(carpeta/Nombre_CSV)
    print("\nDatos originales:\n")
    print(ventas)
    columnas_necesarias = ["fecha", "producto", "categoria", "unidades", "precio_unitario"]
    for col in columnas_necesarias:
        if col not in ventas.columns:
            raise KeyError(f"Falta la columna '{col}'")
except KeyError as e:
    print(f"Error de contenido en el archivo: {e}")

calculo_importe(ventas)

print("\nImporte total: ", ventas_totalesYcategorias(ventas)[0])
print("\nUnidades totales vendidas: ", ventas_totalesYcategorias(ventas)[1])
print("\nImporte total por categoría:\n", ventas_totalesYcategorias(ventas)[2])
print("\n\nUnidades totales por categoría:\n", ventas_totalesYcategorias(ventas)[3])

# A continuachón se aplica un bucle "while" para la consulta del total de ventas por categoría.
# Este bucle sólo se detiene cuando le indicamos que no queremos hacer consulta.
while True:
    consulta = str(input("\n¿Quiere consultar las ventas de alguna categoría en concreto?[si/no]: "))
    if consulta == "si":
        categoria_consulta = str(input("\nEscriba el nombre de la categoría:"))
        if categoria_consulta in list(ventas["categoria"].unique()): # Transforma la serie "categoria" en una lista con las categorías sin repetirse.
            # Esto es porque Pandas utiliza "Series", no listas. Las series no se pueden utilizar en condicionales "if" de la misma manera que las listas.
            suma_importe_categoria = ventas[ventas["categoria"] == categoria_consulta]["importe"].sum() # Guardamos en una variable únicamente las ventas cuya categoría coincida con la seleccionada,
            # y se hace el sumatorio de todas con .sum()
            print(f"\nEl importe total para la categoría '{categoria_consulta}' es: {suma_importe_categoria} €")
        else:
            print("\nLa categoría indicada no existe. Debe escribirla con exactitud.")
        
    elif consulta == "no":
        print("\nConsulta cancelada.")
        break
    else:
        print("\nError: Debe escribir 'si' o 'no'")

try:
    Nombre_parquet = input("\nElige un nombre para guardar los datos en formato .parquet (incluye la extensión): ")
    ventas.to_parquet(carpeta / Nombre_parquet,index=False)
    print("\nSe ha guardado el archivo 'ventas' en formato Parquet")
except:
    print("Error al guardar el archivo .parquet")


ventas_recuperadas = leer_parquet(carpeta / "ventas.parquet")
print("\nDatos recuperados desde Parquet:")
print(ventas_recuperadas)
