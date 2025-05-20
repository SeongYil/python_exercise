import math

a = 0
b = 0
c = 0

# x = (-b ± √(b² - 4ac)) / 2a

denominator = -2 * a
factor = math.sqrt(b**2 - 4 * a * c)
numerator = -b + factor

#리니어 함수
def linear(x):
    return 3 * x + 5

pitagoras = math.sqrt(a**2 + b**2)
print(pitagoras)








a = 10
b = 20

print(a==10)

if (a == 10 and b < a):
    print(b)
    
if type(a) == int:
    print("a is an int")


print(a)

