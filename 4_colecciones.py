# Listas: list
# Colección de elementos ordenados, intercambiables e indexados
# Permite elementos duplicados
mi_lista = [1,2,3,4,5,5,4,3]
print(mi_lista)

mi_lista2 = list(
    ("hola", "bienvenido", "gracias", "adios", "gracias", 3, 4, 5, 5)
)
print(mi_lista2)

# quita y retorna el elemento en la posición indicada, 
# en caso de no indicar la posición, lo hara desde el final de la lista
mi_lista.pop(2) # quita el primer 3
mi_lista.pop() # quita el último 3

# agregar un elemento al final de la lista
mi_lista.append(6)

#mi_lista_ordenada = mi_lista
mi_lista_ordenada = mi_lista.copy()

print("copia de mi lista, antes de ordenar:", mi_lista_ordenada)
mi_lista_ordenada.sort()
print("mi lista original luego de ordenar:", mi_lista)
print("copia de mi lista luego de ordenar:", mi_lista_ordenada)
print("elemento en la posición 2 de mi lista original: ", mi_lista[2])

print("#########################")

# Tuplas: tuples
# Colección de elementos ordenados, pero NO intercambiables, SI indexados
# No permiten agregar o quitar elementos
# Permiten elementos duplicados
mi_tupla = ("Norte", "Centro", "Sur", "Norte")
print("mi tupla: ", mi_tupla)
print("elemento en la posición 2 de mi tupla: ", mi_tupla[2])

# try:
#    mi_tupla.sort()
# except Exception as ex:
#    print(ex)

print("#########################")

# Conjuntos: sets 
# Colección de elementos NO ordenados, NO intercambiables, NO indexados
# Si permiten agregar y quitar elementos
# No permiten elementos duplicados
mi_set = {"Norte", "Centro", "Sur"}
print("mi set: ", mi_set)

mi_set2 = {"Norte", "Centro", "Sur", "sur"}
print("mi set2 (casi duplicado): ", mi_set2)

print("#########################")

# Diccionarios: dict 
# Colección de elementos, de tipo llave=valor
# Ordenados (desde Python 3.7), intercambiables, indexados
# Si permiten agregar y quitar elementos
# No permiten elementos duplicados
mi_diccionario = {
    "zonas": ["Norte", "Centro", "Sur"],
    "pais": "Chile",
    "va al mundial": False,
    "este año": 2022
}
print("mi diccionario: ", mi_diccionario)
print("elemento 'este año' de mi diccionario: ", mi_diccionario["este año"])

# print("elemento en la posición 2 de mi diccionario: ", mi_diccionario[2])
try:
   print("elemento en la posición 2 de mi diccionario: ", mi_diccionario[2])
except Exception as falla:
   print("No se puede acceder por número de indice a un diccionario")
   print("Motivo del error: ", falla)
   # print("Detalle del error: ", falla.with_traceback())

print("""
Llegamos al final de las colecciones...
""")