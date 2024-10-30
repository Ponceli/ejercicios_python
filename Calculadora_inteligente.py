num1 = float(input("Por favor ingrese el primer numero:"))
op = input("Por favor ingrese el operador:")
num2 = float(input("Por favor ingrese el segundo numero:"))



if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2)
elif op == "*":
  print(num1 * num2)
elif op == "/":
  print(num1 / num2)
else:
  print ("Operador invalido, por favor ingreso un operador valido")