
import array

# Crear un arreglo de numeros enteros
edades = array.array('i', [18, 19, 20, 21, 22])

print()

# Mostrar edades
print("Primera edad:", edades[0])
print("Ultima edad:", edades[4])

print()
# Modificar la tercera edad
edades[2] = 25

# Mostrar la edad modificada
print("Nueva tercera edad:", edades[2])

print()
