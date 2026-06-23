import datetime

year_of_birth = int(input("In which year were you born? "))

current_year = datetime.datetime.now().year

current_age = current_year - year_of_birth

print("Your current age is", current_age)

if current_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
