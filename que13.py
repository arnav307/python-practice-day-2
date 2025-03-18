mp=int(input("Enter a price: "))
if mp>10000:
    discount=20
elif 7000<mp<=10000:
    discount=15
else:
    discount=10
    
net_amount=mp-(discount/100)
print(f"Your net amount is {net_amount}")