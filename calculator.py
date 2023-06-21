def basearithmetic(n1, op, n2):
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

def exponents(n1, n2):
     print(n1**n2)

opselection = input("""Enter your choice:
                       Enter 1 for basic arithmetic
                       Enter 2 to calculate exponent
                       """)
        
if opselection == "1":
    basearithmetic(n1=float(input("Enter first number: ")), op=input("Enter your operation: "), n2=float(input("Enter second number: ")))
elif opselection == "2":
    exponents(n1=int(input("Enter base number: ")), n2=int(input("Enter the exponent: ")))
else: 
    print("sod off")
