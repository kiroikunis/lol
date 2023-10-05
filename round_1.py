def multiplication(a,b):
  x = a*b
  return x

def division(a,b):
  x = a/b
  return x

print("dame el primer numero")
a = int(input())
print("dame el segundo numero")
b = int(input())
print("la multiplicacion es", multiplication(a,b), "y la division es", division(a,b))
