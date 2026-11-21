# Exercise 11: University admission
# A student is eligible if (Matric 60% or above and Inter 50% or above), or Entry test 70 or
# above. Take all three and print Eligible or Not eligible.



matric =int(input("Enter % of matric: ")) 
inter =int(input("Enter % of Inter: ")) 
Entry_test =int(input("Enter % of ENtry Test: "))


if matric >= 60 or inter >= 50 or Entry_test >= 70:
    print("Eligible")
else:
    print("Not Eligible")