customer_name = input("customer name:",)
pizza = int(input("pizza:",))
burger = int(input("burger:",))
fried_rice = int(input("fried rice:",))
food = input("food:",)
quantity = int(input("quantity:",))
bill = food * quantity 
if bill>500:
    print("10% offer")
    final_amount = bill/10 * 100
else:
    print("the final amount:",bill)
