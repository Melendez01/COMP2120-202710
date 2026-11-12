
import array

# Crear un arreglo de temperaturas
temperaturas = array.array('i', [28, 30, 29, 31, 27])

# Mostrar temperaturas
print("Primera temperatura:", temperaturas[0])
print("Ultima temperatura:", temperaturas[4])

# Modificar la segunda temperatura
temperaturas[1] = 32

# Mostrar el nuevo valor
print("Nueva segunda temperatura:", temperaturas[1])
