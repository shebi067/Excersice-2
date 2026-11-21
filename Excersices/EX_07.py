
# Take the bill amount and print the discount and the final amount.
# Test: 3000 → Discount: 150.0, Pay: 2850.0


bill_amount = int(input("Enter the billing amount: "))

discount = 0.0

if bill_amount >= 5000:
    discount = bill_amount*0.10
   
elif bill_amount >=2000:
    discount = bill_amount*0.05
    
else:
    discount = 0.0

Total_bill = bill_amount - discount
print(f"Discount, {discount}, \nTotal Amount:{Total_bill}")