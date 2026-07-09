print("Welcome to Electricity Bill Calculator")
units = int(input("Enter the number of units consumed: "))
if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 2
elif units <= 500:
    bill = (100 * 2) + (units - 200) * 3
else:
    bill = (100 * 2) + (300 * 3) + (units - 500) * 5
print("Electricity Bill = ₹", bill)
print("Thank you!")
