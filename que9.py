#9)	Rewrite the following if-else statements using a single if statement and elif:
#if temperature >= 85 and humidity > 60:
#print ('muggy day today')
#else:
#if temperature >= 85:
#print ('warm, but not muggy today')
#else:
#if temperature >= 65:
#print ('pleasant today')
#else:
#if temperature <= 45:
#print ('cold today')
#else:
#print ('cool today')

if temperature >= 85 and humidity > 60:
    print ('muggy day today')
elif temperature >= 85:
        print ('warm, but not muggy today')
elif temperature >= 65:
        print ('pleasant today')
elif temperature <= 45:
        print ('cold today')
else:
    print ('cool today')
