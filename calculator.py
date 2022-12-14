n1=int(input("enter a no"))
n2=int(input("enter a no"))
operator=input("enter operator")
if operator=="add":
    print(n1+n2)
elif operator=="substract":
    print(n1-n2)
elif operator=="multiply":
    print(n1*n2)
elif operator=="division":
    print(n1/n2)
elif operator=="percentage":
    print(n1%n2)
else:
    print("enter valid operator")