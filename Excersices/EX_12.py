# Exercise 12: Ride fare calculator
# Fare = Rs 100 base + Rs 40 per km. At night (hour 22 or later, or before 6), add 20%. Take
# the km and the hour (0–23) and print the final fare.


km = float(input("Enter distance in km: "))
hour = int(input("Enter hour (0-23): "))

fare = 100 + (40 * km)

if hour >= 22 or hour < 6:
    fare = fare + (fare * 0.20)   # ya fare *= 1.20

print("Final fare: Rs", fare)