print("Welcome to ATM")
pin = int(input("Enter your 4-digit PIN: "))
if pin == 1234:
    print("Access Granted")
    print("Welcome!")
else:
    print("Incorrect PIN")
    print("Try Again")
