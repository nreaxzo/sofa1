import math

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
h = float(input("Enter step h: "))

def f(x):
    return 7 - x * math.exp(2 * x - 1) + math.sqrt(abs(x))

values_while = []
x = a
while x <= b:
    values_while.append(f(x))
    x += h

print("\nCalculation results (while loop):")
print(values_while)

