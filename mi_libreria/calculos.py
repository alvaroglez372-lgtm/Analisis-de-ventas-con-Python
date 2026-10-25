def calculo_importe(datos):
    # Creación de una nueva columna de datos con el importe de cada producto.
    datos['importe'] = datos['unidades'] * datos['precio_unitario']
    return datos['importe']

def ventas_totalesYcategorias(datos):
    # Calcula el importe y las unidades totales y por categorías.
    importe_total = datos["importe"].sum()
    unidades_totales = datos["unidades"].sum()
    ventasXcategoria = datos.groupby("categoria")["importe"].sum()
    unidadesXcategoria = datos.groupby("categoria")["unidades"].sum()
    totales_categoria = [importe_total, unidades_totales, ventasXcategoria, unidadesXcategoria]
    return totales_categoria

