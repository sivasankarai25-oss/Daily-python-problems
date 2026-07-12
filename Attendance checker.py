print("Welcome to Attendance Checker")
total_days = int(input("Enter total working days: "))
attended_days = int(input("Enter days attended: "))
attendance = (attended_days / total_days) * 100
print("Attendance:", attendance, "%")
if attendance >= 75:
    print("Eligible to write the exam")
else:
    print("Not eligible to write the exam")
print("Thank you!")
