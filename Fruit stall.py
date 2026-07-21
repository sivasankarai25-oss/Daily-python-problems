print("Welcome to Fruit Stall")
fruit = input("Enter fruit name (apple/grapes/orange): ")
kg = int(input("Enter the weight (kg): "))
if fruit == "apple":
    bill = kg * 150
elif fruit == "grapes":
    bill = kg * 120
elif fruit == "orange":
    bill = kg * 100
else:
    bill = 0
    print("Fruit not available")
print("The bill is:", bill)
