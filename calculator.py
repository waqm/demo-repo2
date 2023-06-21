n1 = float(input("Enter first number: "))
op = input("Enter your operation: ")
n2 = float(input("Enter second number: "))

if op == "+":
    print(n1+n2)
elif op == "-":
    print(n1-n2)
elif op == "*":
    print(n1*n2)
elif op == "/":
    print(n1/n2)
else:
    print ("Invalid operation!!")