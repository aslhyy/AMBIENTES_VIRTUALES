# Calcula el promedio de una lista de números.

def calcular_promedio(numeros):
    """Calcula el promedio de una lista de números."""
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

# Ejemplo de uso
lista_numeros = [5, 8, 12, 3, 9]
promedio = calcular_promedio(lista_numeros)

print("Lista de números:", lista_numeros)
print("El promedio es:", promedio)
