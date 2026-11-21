

# Exercise 8: Character type
# Take one character and print whether it is a Vowel, Consonant, Digit or Special character.
# Hint: .isdigit(), .isalpha(), and .lower() in "aeiou".

# Test: e → Vowel · 7 → Digit · K → Consonant · @ → Special character




user = input("Enter a number: ")

if len(user) !=1:
    print("Enter only a one character")
elif user.isdigit():
    print("Digit")
elif user.isalpha():
    if user.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Speacial Character")


