weight=float(input("Enter your weight in (kg)"))
height=float(input("Enter your height "))
height_cm=height/100
bmi=weight/height_cm**2
print(f"Your BMI is {bmi}")
if bmi<18.5:
    print("Underweight")
elif 18.5<=bmi<25:
    print("normal weight")
elif 25<=bmi<30:
    print("overweight")
else:
    print("obese")

    
