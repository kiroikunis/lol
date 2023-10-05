def triangle_area(a,b):
  x = (a*b)/int(2)
  return x

print("how much is the base")
a = int(input())
print("and how much is the hight?")
b = int(input())
print("there you gou", triangle_area(a,b), "that is your area")
