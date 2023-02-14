born_year = int(input("Enter the year you were born in? "))
this_year = int(input("Enter current year? "))
age = this_year - born_year
if age >= 18:
    print("Congrats you are old enough.")
