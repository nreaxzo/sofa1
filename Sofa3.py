import math

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
h = float(input("Enter step h: "))

def f(x):
    return 7 - x * math.exp(2 * x - 1) + math.sqrt(abs(x))

values = []
x = a
while x <= b:
    fx = f(x)
    values.append(fx)
    x += h

print("\nList of function values (row):")
print(values)

duplicates = set([value for value in values if values.count(value) > 1])
print("\nDuplicate function values:")
for duplicate in duplicates:
    print(duplicate)

