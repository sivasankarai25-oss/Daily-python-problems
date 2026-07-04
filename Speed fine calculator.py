print("Welcome to Speed Fine Calculator")
speed = int(input("Speed of the vehicle: "))
if speed <= 50:
    print("No fine. Have a nice day!")
elif speed < 120:
    print("Fine: ₹500")
else:
    print("Fine: ₹2000")
print("Have a nice journey. Drive safely!")
