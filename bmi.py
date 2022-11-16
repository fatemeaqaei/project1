weight=float(input("enter your weight(kg): "))
height=float(input("enter your height(m): "))
if weight<=0 or height<=0:
    print("wrong input")
else:
    bmi=weight/height**2

    if bmi<18.5:
        print("underweight")
    elif bmi>=18.5 and bmi <=24.9:
        print("normal weight")
    elif bmi >=25 and bmi <=29.9:
        print("overweight")
    elif bmi >=30 and bmi <=34.9:
        print("obesity")
    elif bmi >=35 and bmi <=39.9:
        print("extreme obesity")