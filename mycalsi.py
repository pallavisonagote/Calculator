import cmath
from _ast import arg
from switchcase import switch

print(
    "****************************************************************************************************************")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tCalculator")
print(
    "****************************************************************************************************************")

print("\n\n")

print(" To ADD press : +\n"
      " To SUB press :-\n"
      " To MUL press : *\n"
      " To DIV press : /\n"
      " To find Sqr Root press : ^(1/2) \n"
      " To find Square press : ^(2)\n"
      " To find Area of Triangle press : area\n"
      " To find Quadratic press : quad\n"
      " To Exit press : q")
print("Enter")
a = float(input())

i = 0

while 1 == 1:
    op = input()
    if op == "q":
        break
    elif op == "^(1/2)":
        a = a ** 0.5
        print(a)
        continue
    elif op == "^2":
        a = a ** 2
        continue
    elif op == "area":
        y = float(input('Enter second side: '))
        z = float(input('Enter third side: '))

        # calculate the semi-perimeter
        s = (a + y + z) / 2

        # calculate the area
        area = (s * (s - a) * (s - y) * (s - z)) ** 0.5

        print(area)
        continue
    elif op == "quad":
        f = float(input('Enter b: '))
        g = float(input('Enter c: '))

        # calculate the discriminant
        d = (f ** 2) - (4 * a * g)

        # find two solutions
        sol1 = (-f - cmath.sqrt(d)) / (2 * a)
        sol2 = (-f + cmath.sqrt(d)) / (2 * a)
        print(format(sol1, sol2))


    else:
        b = float(input())
        try:
            if op == "+":
                a = a + b
                print("________")
            elif op == "-":
                a = a - b
                print("________")
            elif op == "*":
                a = a * b
                print("________")
            elif op == "/":
                a = a / b
                print("________")

            else:
                print("Invalid........")
        except Exception as e:
            print(e)

        print(" ", a)
        i = i + 1
