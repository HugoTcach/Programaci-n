print("Actividades:")
print("=" * 30)

# Actividad 1: Imprimir números del 0 al 100
print("\nActividad 1: Imprimir números del 0 al 100")
# Utilizamos un bucle for para iterar a través de la secuencia de números generada por range(0, 101).
# range(0, 101) genera números desde 0 hasta 100 (el segundo argumento es exclusivo).
for numero in range(0, 101):
    # Imprimimos cada número en una línea diferente.
    print(numero)

# Actividad 2: Contar dígitos de un número entero
print("\nActividad 2: Contar dígitos de un número entero")
# Solicitamos al usuario que ingrese un número entero.
while True:
    try:
        numero_str = input("Ingrese un número entero: ")
        # Intentamos convertir la entrada a un entero. Si falla, se lanza una excepción ValueError.
        int(numero_str)
        # Si la conversión es exitosa, salimos del bucle.
        break
    except ValueError:
        # Si la entrada no es un entero válido, mostramos un mensaje de error.
        print("Entrada inválida. Por favor, ingrese un número entero.")

# La cantidad de dígitos de un número entero (en formato string) es simplemente la longitud de la cadena.
cantidad_digitos = len(numero_str)
# Mostramos la cantidad de dígitos al usuario.
print(f"El número {numero_str} tiene {cantidad_digitos} dígitos.")

# Actividad 3: Sumar números entre dos valores dados por el usuario (excluyéndolos)
print("\nActividad 3: Sumar números entre dos valores dados por el usuario (excluyéndolos)")
# Solicitamos al usuario que ingrese dos números enteros.
while True:
    try:
        valor1 = int(input("Ingrese el primer número entero: "))
        valor2 = int(input("Ingrese el segundo número entero: "))
        # Si las entradas son válidas, salimos del bucle.
        break
    except ValueError:
        # Si alguna de las entradas no es un entero válido, mostramos un mensaje de error.
        print("Entrada inválida. Por favor, ingrese números enteros.")

# Determinamos el rango de números a sumar.
# Usamos min() y max() para asegurarnos de que el bucle funcione correctamente sin importar el orden de los valores.
inicio = min(valor1, valor2) + 1
fin = max(valor1, valor2)

# Inicializamos la variable para almacenar la suma.
suma_entre_valores = 0
# Utilizamos un bucle for para iterar a través de los números en el rango (excluyendo los extremos).
for numero in range(inicio, fin):
    # Sumamos cada número a la variable 'suma_entre_valores'.
    suma_entre_valores += numero

# Mostramos la suma de los números comprendidos entre los dos valores.
print(f"La suma de los números entre {valor1} y {valor2} (excluyéndolos) es: {suma_entre_valores}")

# Actividad 4: Sumar números ingresados por el usuario hasta que ingrese 0
print("\nActividad 4: Sumar números ingresados por el usuario hasta que ingrese 0")
# Inicializamos la variable para almacenar la suma acumulada.
suma_acumulada = 0
# Utilizamos un bucle while que continuará hasta que el usuario ingrese 0.
while True:
    try:
        numero_ingresado = int(input("Ingrese un número entero (ingrese 0 para detener): "))
        # Si el número ingresado es 0, salimos del bucle.
        if numero_ingresado == 0:
            break
        # Si el número no es 0, lo sumamos a la suma acumulada.
        suma_acumulada += numero_ingresado
    except ValueError:
        # Si la entrada no es un entero válido, mostramos un mensaje de error.
        print("Entrada inválida. Por favor, ingrese un número entero.")

# Mostramos el total acumulado.
print(f"El total de los números ingresados es: {suma_acumulada}")

# Actividad 5: Juego de adivinar un número aleatorio
import random

print("\nActividad 5: Juego de adivinar un número aleatorio (entre 0 y 9)")
# Generamos un número aleatorio entre 0 y 9 (inclusive).
numero_secreto = random.randint(0, 9)
# Inicializamos el contador de intentos.
intentos = 0
# Utilizamos un bucle while que continuará hasta que el usuario adivine el número.
while True:
    try:
        intento = int(input("Intenta adivinar el número (entre 0 y 9): "))
        # Incrementamos el contador de intentos.
        intentos += 1
        # Comparamos el intento del usuario con el número secreto.
        if intento == numero_secreto:
            # Si el usuario adivina correctamente, mostramos un mensaje y salimos del bucle.
            print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
            break
        elif intento < numero_secreto:
            # Si el intento es menor, damos una pista.
            print("El número secreto es mayor.")
        else:
            # Si el intento es mayor, damos una pista.
            print("El número secreto es menor.")
    except ValueError:
        # Si la entrada no es un entero válido, mostramos un mensaje de error.
        print("Entrada inválida. Por favor, ingrese un número entero entre 0 y 9.")

# Actividad 6: Imprimir números pares del 0 al 100 en orden decreciente
print("\nActividad 6: Imprimir números pares del 0 al 100 en orden decreciente")
# Utilizamos un bucle for con la función range() para generar números pares en orden decreciente.
# range(100, -1, -2) comienza en 100, termina en -1 (exclusivo, por lo que llega a 0), y decrementa de 2 en 2.
for numero_par in range(100, -1, -2):
    # Imprimimos cada número par.
    print(numero_par)

# Actividad 7: Calcular la suma de números del 0 a un número entero positivo ingresado por el usuario
print("\nActividad 7: Calcular la suma de números del 0 a un número entero positivo indicado por el usuario")
# Solicitamos al usuario que ingrese un número entero positivo.
while True:
    try:
        limite = int(input("Ingrese un número entero positivo: "))
        # Verificamos si el número es positivo.
        if limite > 0:
            # Si es positivo, salimos del bucle.
            break
        else:
            # Si no es positivo, mostramos un mensaje de error.
            print("Por favor, ingrese un número entero positivo.")
    except ValueError:
        # Si la entrada no es un entero válido, mostramos un mensaje de error.
        print("Entrada inválida. Por favor, ingrese un número entero.")

# Inicializamos la variable para la suma.
suma_hasta_limite = 0
# Utilizamos un bucle for para iterar desde 0 hasta el límite (inclusive).
for numero in range(limite + 1):
    # Sumamos cada número a la variable 'suma_hasta_limite'.
    suma_hasta_limite += numero

# Mostramos la suma total.
print(f"La suma de los números desde 0 hasta {limite} es: {suma_hasta_limite}")

# Actividad 8: Contar pares, impares, positivos y negativos de 100 números ingresados
print("\nActividad 8: Contar pares, impares, positivos y negativos de 100 números ingresados")
# Definimos la cantidad de números a ingresar (para probar, puedes cambiarlo a un número menor).
cantidad_numeros = 5 # Para probar, puedes usar un número menor como 5
pares = 0
impares = 0
positivos = 0
negativos = 0

# Utilizamos un bucle for para solicitar al usuario que ingrese la cantidad de números definida.
for i in range(cantidad_numeros):
    while True:
        try:
            numero_ingresado = int(input(f"Ingrese el número {i + 1}: "))
            # Verificamos si el número es par o impar.
            if numero_ingresado % 2 == 0:
                pares += 1
            else:
                impares += 1
            # Verificamos si el número es positivo o negativo.
            if numero_ingresado > 0:
                positivos += 1
            elif numero_ingresado < 0:
                negativos += 1
            # Si la entrada es válida, salimos del bucle interno.
            break
        except ValueError:
            # Si la entrada no es un entero válido, mostramos un mensaje de error.
            print("Entrada inválida. Por favor, ingrese un número entero.")

# Mostramos los resultados del conteo.
print(f"\nDe los {cantidad_numeros} números ingresados:")
print(f"  - Pares: {pares}")
print(f"  - Impares: {impares}")
print(f"  - Positivos: {positivos}")
print(f"  - Negativos: {negativos}")

# Actividad 9: Calcular la media de 100 números ingresados
print("\nActividad 9: Calcular la media de 100 números ingresados")
# Definimos la cantidad de números a ingresar (para probar, puedes cambiarlo a un número menor).
cantidad_numeros_media = 5 # Para probar, puedes usar un número menor como 5
suma_total_media = 0

# Utilizamos un bucle for para solicitar al usuario que ingrese la cantidad de números definida.
for i in range(cantidad_numeros_media):
    while True:
        try:
            numero_ingresado = int(input(f"Ingrese el número {i + 1} para calcular la media: "))
            # Sumamos el número ingresado a la suma total.
            suma_total_media += numero_ingresado
            # Si la entrada es válida, salimos del bucle interno.
            break
        except ValueError:
            # Si la entrada no es un entero válido, mostramos un mensaje de error.
            print("Entrada inválida. Por favor, ingrese un número entero.")

# Calculamos la media.
if cantidad_numeros_media > 0:
    media = suma_total_media / cantidad_numeros_media
    # Mostramos la media.
    print(f"\nLa media de los {cantidad_numeros_media} números ingresados es: {media}")
else:
    # Si no se ingresaron números, mostramos un mensaje.
    print("\nNo se ingresaron números para calcular la media.")

# Actividad 10: Invertir el orden de los dígitos de un número
print("\nActividad 10: Invertir el orden de los dígitos de un número")
# Solicitamos al usuario que ingrese un número entero.
while True:
    try:
        numero_para_invertir = input("Ingrese un número entero para invertir sus dígitos: ")
        # Intentamos convertir la entrada a un entero para verificar que sea un número.
        int(numero_para_invertir)
        # Si la conversión es exitosa, salimos del bucle.
        break
    except ValueError:
        # Si la entrada no es un entero válido, mostramos un mensaje de error.
        print("Entrada inválida. Por favor, ingrese un número entero.")

# Convertimos el número a una cadena para poder invertir sus caracteres.
numero_str_invertir = str(numero_para_invertir)
# Invertimos la cadena utilizando slicing con un paso de -1.
numero_invertido_str = numero_str_invertir[::-1]
# Mostramos el número invertido.
print(f"El número {numero_para_invertir} invertido es: {numero_invertido_str}")