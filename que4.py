#4)	Write a program to check whether a character is a vowel or consonant. [Expected from user’s input].
character=input("Enter a letter either vowel or consonant: ").lower()
if character.isalpha() and len(character)==1:
    
    if character in ['a','e','i','o','u']:
        print("The letter is vowel")
    else:
        print("The letter is consonant")
else:
    print("please enter valid input")