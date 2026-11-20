a = int(input("First number: "))
b = int(input("Second number: "))
c = input("What to do + - * / : ")

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
else:
    print(a / b)