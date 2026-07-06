print("welcome to the food order calculator")
burgers=int(input("one burger amount is:"))
quantity=int(input("the number of burgers you buy:"))
bill=quantity*burgers
print("the bill is:",bill)
if bill>=500:
    print("you get a free fruit juice")
    print("thankyou for using food order calculator")
else:
    print("better luck next time!")
    print("thankyou for using food order calculator")
