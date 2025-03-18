'''#a)The user enters either 'A', 'B', or 'C'. If 'A' is entered, the program should display the word 'Apple'; if 'B' is entered, it displays 'Banana'; and if 'C' is entered, it displays 'Coconut'. Use nested if statements for this.
user=input("Enter either A,B or C: ")
if user=='A':
    print("Apple")
elif user=='B':
    print('Banana')
elif user=='C':
    print("Coconut")
else:
    print("Invalid inputs")
    
#A student enters the number of college credits earned. If the number of credits is greater than or equal to 90, 'Senior Status' is displayed; if greater than or equal to 60, 'Junior Status' is displayed; if greater than or equal to 30, 'Sophomore Status' is displayed; else, 'Freshman Status' is displayed
credit=int(input("Enter a credits: "))
if credit>=90:
    print("Senior Status")
elif credit>=60:
    print("Junior Status")
elif credit>=30:
    print("Sophomore Status")
else:
    print("freshman Status")'''
    
#The user enters a number. If the number is divisible by 3, the word ‘Fizz’ should be displayed; if the number is divisible by 5 the word ‘Buzz’ should be displayed and if the number is divisible by both ‘FizzBuzz’ should be displayed.
num=int(input("Enter a number: "))
if num%5==0 and num%3==0:
    print("FizzBuzz")
elif num%5==0:
    print("Buzz")
elif num%3==0:
    print("Fizz")
else:
    print("It is not divisible by bothe 5 and 3")