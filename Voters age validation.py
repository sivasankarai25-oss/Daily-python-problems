import datetime

year_of_birth = int(input("Enter your birth year: "))

current_year = datetime.datetime.now().year
if year_of_birth > current_year or year_of_birth < 1900:
    print("Invalid birth year!")
else:
    current_age = current_year - year_of_birth
    print("Your current age is", current_age)

    
    if current_age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")
