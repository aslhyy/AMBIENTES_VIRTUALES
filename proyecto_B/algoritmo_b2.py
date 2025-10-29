# Crea un DataFrame con pandas y realiza operaciones básicas.

import pandas as pd

# Crear un DataFrame de ejemplo con datos de ventas
datos = {
    "Producto": ["Hamburguesa", "Perro Caliente", "Arepa", "Mazorcada", "Carne en salsa"],
    "Precio": [12000, 10000, 8000, 9000, 15000],
    "Unidades Vendidas": [20, 35, 25, 15, 18]
}

df = pd.DataFrame(datos)

# Mostrar el DataFrame
print("Tabla de ventas:\n")
print(df)

# Calcular total de ingresos por producto
df["Total Ingreso"] = df["Precio"] * df["Unidades Vendidas"]

print("\nTabla con ingresos totales:\n")
print(df)

# Mostrar estadísticas básicas
print("\nEstadísticas descriptivas:\n")
print(df.describe())

# Filtrar productos con ingresos mayores a 200000
filtro = df[df["Total Ingreso"] > 200000]
print("\nProductos con ingresos mayores a 200000:\n")
print(filtro)
