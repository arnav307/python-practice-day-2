#7)	Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

num1=int(input("Enter a number: "))
num2=17
difference_num=num1-num2
difference=abs(difference_num)

if difference>17:
    print(f"{2*difference}")
else:
    print(f"{difference}")