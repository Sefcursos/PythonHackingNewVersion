# Leer un número natural del usuario
c0 = int(input("Ingresa un número natural (mayor que 0): "))

# Verificamos que el número sea válido
if c0 <= 0:
    print("El número debe ser un entero positivio mayor que cero.")

else:
    pasos = 0
    print(f"Secuencia de Collatz para {c0}")

    while c0 != 1:
        print(c0)
        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1
        pasos += 1

    print(1) # Imprimimos el último valor (1)
    print(f"Número de pasos: {pasos}")
