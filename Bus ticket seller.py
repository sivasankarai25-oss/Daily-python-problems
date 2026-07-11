print("Welcome to the Bus Ticket Calculator")
place = input("Enter your destination: ")
if place == "Chennai":
    print("Ticket Price: ₹50")
elif place == "Vellore":
    print("Ticket Price: ₹120")
elif place == "Madurai":
    print("Ticket Price: ₹350")
elif place == "Coimbatore":
    print("Ticket Price: ₹500")
else:
    print("Sorry, bus service is not available to this destination.")
print("Have a safe journey!")
