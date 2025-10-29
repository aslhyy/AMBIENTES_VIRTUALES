# Calcula promedio, valor máximo y mínimo de una lista de datos.

def calcular_estadisticas(lista):
    """Calcula promedio, máximo y mínimo de una lista."""
    promedio = sum(lista) / len(lista)
    maximo = max(lista)
    minimo = min(lista)
    return promedio, maximo, minimo

# Lista de ejemplo
datos = [10, 25, 18, 30, 22, 15, 40]

promedio, maximo, minimo = calcular_estadisticas(datos)

print("Datos:", datos)
print("Promedio:", promedio)
print("Máximo:", maximo)
print("Mínimo:", minimo)
