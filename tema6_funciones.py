def sumar(num1, num2):
  return num1 + num2

def restar(num1, num2):
  return num1 - num2

def multiplicar(num1, num2):
  return num1 * num2

def dividir(num1, num2):
  if num2 == 0:
    return 
  else:
    return num1 / num2

while True:
  print("\nCalculadora")
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Dividir")
  print("Otro número: Salir")

  try:
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
      num1 = float(input("Ingresa el primer número: "))
      num2 = float(input("Ingresa el segundo número: "))
      resultado = sumar(num1, num2)
    elif opcion == 2:
      num1 = float(input("Ingresa el primer número: "))
      num2 = float(input("Ingresa el segundo número: "))
      resultado = restar(num1, num2)
    elif opcion == 3:
      num1 = float(input("Ingresa el primer número: "))
      num2 = float(input("Ingresa el segundo número: "))
      resultado = multiplicar(num1, num2)
    elif opcion == 4:
      num1 = float(input("Ingresa el primer número: "))
      num2 = float(input("Ingresa el segundo número: "))
      resultado = dividir(num1, num2)
    else:
      print("Saliendo...")
      break

    print(f"El resultado es: {resultado}")
  except ValueError:
    print("Opción inválida. Por favor, ingresa un número.")