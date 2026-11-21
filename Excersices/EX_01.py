
# Exercise 1: Positive, negative or zero
# Take a number and print whether it is Positive, Negative or Zero.
# Test: -7 → Negative



number = int(input("Enter your number: "))

if number == 0:
    print("The number is zero")
elif number < 0:
    print("The number is Negative")
elif number > 0:
    print("The number is Positive")

