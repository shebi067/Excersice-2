# Take three sides. If any two sides add up to no more than the third, print “Not a valid
# triangle”. Otherwise print its type: Equilateral (all equal), Isosceles (two equal) or Scalene
# (none equal).


a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Not a valid triangle")
else:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
        