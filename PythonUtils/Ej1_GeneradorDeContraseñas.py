# Ejercicio 1: Generador de Contraseñas Seguras, Objetivo: Crear un Script en Python que genere contraseñas aleatorias y seguras usando letras, números y símbolos.

# Herramientas: random: para seleccionar caracteres aleatorios. string: para obtener listas de caracteres alfabéticos, numéricos y símbolos.

import random
import string

def generar_contraseña(longitud=12):
    # Usamos posibles: letras mayúsculas, minúsculas, dígitos y símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Usamos random.choice para seleccionar caracteres aleatorios
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))

    return contrasena

# Prueba generando contraseñas de distintas longitudes
print("Contraseña de 12 caracteres:", generar_contraseña(12))
print("Contraseña de 20 caracteres:", generar_contraseña(20))