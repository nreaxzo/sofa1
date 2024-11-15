import math

a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))
h = float(input("Enter step h: "))

def f(x):
    return 7 - x * math.exp(2 * x - 1) + math.sqrt(abs(x))

values_for = []
for x in range(int(a * 100), int(b * 100), int(h * 100)):
    x /= 100 
    values_for.append(f(x))

print("Calculation results (for loop):")
print(values_for)

