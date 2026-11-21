# Take the balance and the package price. If the balance is enough, print “Package
# activated” and the remaining balance. Otherwise, print how much more is needed.
# Test: balance 300, price 450 → Insufficient balance, need Rs 150 more


print("Chose the package list below!")
print("1. Standar - Price: 250")
print("2. Diamond - Price: 350")
print("3. Platinum - Price: 450")

user = int(input("Enter the balance: "))
user1 = int(input("Enter the package Number (1/2/3): "))

if user1 == 1:
    price = 250
elif user1 == 2:
    price = 350
elif user1 == 3:
    price = 450
else:
    price = None

if price is None:
    print("Enter a valid number")
elif user >= price:
    remaining = user - price
    print("Package activated")
    print("Remaining balance:", remaining)
else:
    needed = price - user
    print("Insufficient balance, need Rs", needed, "more")



