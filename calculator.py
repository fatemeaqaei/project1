import math 

print("+ : sum","      - : sub","      * : mul","      / : div" )
print()
print("                           or")
print()
print("sin","    cos","    tan","    cot","    sqrt","    log","    fact")
print()
op=input("enter your choice: ")

if op == "+" or op == "*" or op == "-" or op == "/":
    x = float(input("Please enter your first number : "))
    y = float(input("Please enter your second number : "))
elif op == "sin" or op == "cos" or op == "tan" or op == "cot" or op =="fact" or op =="sqrt" or op =="log":
    x = int(input("Please enter your number : "))

if op=='+':
    result=x+y
    print(result)
elif op=='-':
    result=x-y
    print(result)
elif op=='*':
    result=x*y
    print(result)
elif op=='/':
    if y==0:
        result="wrong number"
    else:    
        result=x/y
    print(result)
elif op=='sin':
    result = math.sin(math.radians(x))
    print(result)
elif op=='cos':
    result = math.cos(math.radians(x))
    print(result)
elif op=='tan':
    result = math.tan(math.radians(x))
    print(result)
elif op=='cot':
    result =1/ math.tan(math.radians(x))
    print(result)
elif op == "sqrt":
    if x>0:
        result = math.sqrt(x)
        print(result)
    else:
        print("error")
elif op=='log':
    result = math.log(x)
    print(result)
elif op == 'fact':
    result = math.factorial(x)
    print("the result is: ",result)    