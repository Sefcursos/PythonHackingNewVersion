# Ejercicio 2: Verificador de Fuerza de Contraseñas, OBJETIVO: Evaluar si una contraseña es débil, media o fuerte según ciertos criterios como longitud, uso de mayúsculas, minúsculas, números y símbolos.
# Criterios de evaluación: 1. Longitud mínima de 8 caracteres, 2. Contiene letras minúsculas, 3. Contiene letras mayúsculas, 4. Contiene números, 5. Contiene símbolos.

# Llamamos de la libreria string
import string
import getpass
import tkinter
from tkinter import messagebox

# Creamos nuestra funcion para evaluar si la contraseña cumple las condiciones requeridas, nivel de criticidad
def evaluar_contraseña(contraseña):
    longitud = len(contraseña)
    tiene_mayusculas = any(c.isupper() for c in contraseña)
    tiene_minusculas = any(c.islower() for c in contraseña)
    tiene_numeros = any(c.isdigit()for c in contraseña)
    tiene_simbolos = any(c in string.punctuation for c in contraseña)
  # tiene_letra= any(c.isalpha() for c in contraseña)

    # Comprobamos si nuestra contraseña reune las condiciones necesarias para ser debíl, fuerte o cremita.
    puntos = 0
    if longitud >= 8:
        puntos += 1
    if tiene_mayusculas:
        puntos += 1
    if tiene_minusculas:
        puntos +=1
    if tiene_numeros:
        puntos += 1
    if tiene_simbolos:
        puntos += 1

    # if tiene_mayuscula and tiene_simbolo and tiene_numero:
    #     return ("Tu contraseña es cremita")
    # elif tiene_mayuscula and tiene_simbolo:
    #     return("Tu contraseña esta fuerte")
    # elif tiene_letra:
    #     return ("Podrias esforzarte más")
    # else:
    #     return ("Te van a jakear amigo")

    # Verificamos si se dan las condiciones necesarias
    if puntos <= 2:
        nivel = "Podrías esforzarte más"
    elif puntos == 3 or puntos  == 4:
        nivel = "Tu contraseña esta fuerte, bueeenoooo!!!!"
    else:
        nivel = "Tu contraseña es cremita"

    # Recomendaciones
    recomendaciones = []
    if longitud < 8:
        recomendaciones.append("Usa al menos 8 caracteres.")
    if not tiene_mayusculas:
        recomendaciones.append("Agrega al menos una letra mayúscula.")
    if not tiene_minusculas:
        recomendaciones.append("Agrega al menos una letra minúscula")
    if not tiene_numeros:
        recomendaciones.append("Ingresa al menos un número.")
    if not tiene_simbolos:
        recomendaciones.append("Incluye símbolos (como @, #, !, etc.)")

    return nivel, recomendaciones

def analizar():
    contraseña = entrada.get()
    if not contraseña:
        messagebox.showwarning("Advertencia", "Por favor, Ingresa tu contraseña.")
        return
    nivel, recomendaciones = evaluar_contraseña(contraseña)
    resultado.config(text=f"Nivel de seguridad: {nivel}")

    if recomendaciones:
        texto = "Recomendaciones:\n" + "\n".join(f"* {r}" for r in recomendaciones)
    else:
        texto = "¡Tu contraseña es mucha cremita"

    detalles.config(text=texto)

# Inferfaz Tkinter
ventana = tkinter.Tk()
ventana.title("Verificador de contraseña")
ventana.geometry("500x400")
ventana.resizable(False, False)

tkinter.Label(ventana, text="Ingresa una contraseña:", font=("Arial", 12)).pack(pady=10)
entrada = tkinter.Entry(ventana, show="*", width=30, font=("Arial", 12))
entrada.pack()

tkinter.Button(ventana, text="Verificar", command=analizar, font=("Arial", 12)).pack(pady=10)

resultado = tkinter.Label(ventana, text="", font=("Arial", 14, "bold"))
resultado.pack(pady=5)

detalles = tkinter.Label(ventana, text="", font=("Arial", 14, "bold"), justify="left", wraplength=350)
detalles.pack(pady=5)

ventana.mainloop()

# Entrada oculta para mayor privacidad
# try:
#     contraseña = getpass.getpass("Ingresa tu contraseña (oculta): ")
# except Exception as e:
#     print(" Error al usar getpass. Volviendo al input normal.")
#     contraseña = input("Ingresa tu contraseña: ")
#
# nivel, consejos = evaluar_contraseña(contraseña)
#
# print(f"\nNivel de seguridad: {nivel}")
# if consejos:
#     print("Recomendaciones para mejorar: ")
#     for rec in consejos:
#         print(f" - {rec}")
# else:
#     print("¡Tu contraseña es una mega cremita! ")
# # Entrada del usuario
# contraseña = input("Introduce la contraseña para verificar su fuerza😊: ")
# resultado = evaluar_contraseña(contraseña)
# print(resultado)