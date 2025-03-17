#3)	Write a program to find the lowest number out of two numbers expected from the user.
num1=int(input("Enter a first number: "))
num2=int(input("Enter a second number: "))
if num1<num2:
    print(f"{num1} is lowest number")
elif num2<num1:
    print(f"{num2} is lowest number")
else:
    print(f"both are same")