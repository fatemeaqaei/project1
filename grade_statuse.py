name=input("enter student name: ")
family=input("enter studebt family: ")

a=float(input("enter first grade: "))
b=float(input("enter second grade: "))
c=float(input("enter third grade: "))

grade=(a+b+c)/3

if grade>=17:
    print("the level is great")
elif grade<17 or grade>=12:
    print("the level is normal")
elif grade<12:
    print("the level is fail")
