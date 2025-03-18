user_input = int(input("Enter units: "))

if user_input <= 100:
    print("It's free!!!")
    units = 0
elif 101 <= user_input <= 300:
    units = (user_input - 100) * 2
elif user_input > 300:
    units = 400 + (user_input - 300) * 5

print(f"The total bill is {units}")

    