gender = input("Enter either M/F (M for male and F for female): ").lower()
age = int(input("Enter your age: "))

if 18 <= age < 30:
    if gender == 'm':
        print("The wage is Rs 700")
    elif gender == 'f':
        print("The wage is Rs 750")
    else:
        print("Invalid gender. Please enter M for male or F for female.")
        
elif 30 <= age <= 40:
    if gender == 'm':
        print("The wage is Rs 800")
    elif gender == 'f':
        print("The wage is Rs 850")
    else:
        print("Invalid gender. Please enter M for male or F for female.")
else:
    print("Age is out of valid range (18 to 40).")


