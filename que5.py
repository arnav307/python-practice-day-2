#5)	Accept the age of 4 people and display the oldest one.
ram=int(input("Enter age of ram: "))
hari=int(input("Enter age of hari: "))
gopal=int(input("Enter age of gopal: "))
krishna=int(input("Enter age of krishna: "))
if ram>hari and ram>gopal and ram>krishna:
    print(f"Ram is oldest")
elif hari>ram and hari>gopal and hari>krishna:
    print(f"hari is oldest")
elif gopal>ram and gopal>hari and gopal>krishna:
    print(f"gopal is oldest")
elif krishna>ram and krishna>hari and krishna>gopal:
    print(f"krishna is oldesr ")