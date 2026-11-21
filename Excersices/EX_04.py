

# Check whether a number is divisible by both 5 and 11. Use % and and.
# Test: 55 → Yes · 25 → No




number = int(input("Enter a number: "))

if number % 5 == 0 and number % 11 == 0:
    print("Yes")
else:
    print("No")
