
# Take a student’s marks out of 100. 40 or above is Pass; below 40 is Fail.
# Test: 38 → Fail



marks = int(input("Enter your marks: "))

if marks >=40 and marks <= 100:
    print("Pass")
elif marks < 40:
    print("Fail")
else:
    print("Enter a Valid Marks")

    