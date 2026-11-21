
# Take a person’s age. At 18 or above, print “Eligible to vote”. Otherwise, print how many
# years are left.
# Test: 15 → Not eligible, wait 3 more years

age = int(input("enter your age: "))

if age >= 18:
    print ("You are eligible")
else:
    years_left = 18 - age
    print(f"you are not eligible to vote, wait for {years_left} years!")

