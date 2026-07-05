print("Welcome to the ATM")
balance = int(input("Enter the balance amount: "))
withdrawal = int(input("Enter the withdrawal amount: "))
if withdrawal <= balance:
    balance = balance - withdrawal
    print("Remaining balance:", balance)
else:
    print("Insufficient balance!")
print("Thanks for using the ATM")
