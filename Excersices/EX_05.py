

# Exercise 5: Weather advice
# Take the temperature in °C and print the advice.
# Test: 38 → Very hot, stay hydrated




temp = int(input("Enter the temparature in Celcius: "))

if temp <10:
    print("Cold, wear a jacket")
elif temp <=25:
    print("Pleasant")
elif temp <=35:
    print("warm")
else:
    print("Very hot, stay hyderated")

    
