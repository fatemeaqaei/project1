a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))

if c<=a+b and b<=a+c and a<=b+c:
    print("it is possible")
else:
     print("it is not possible")