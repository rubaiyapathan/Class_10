year = int(input("Enter the year (4 digit ti check):"))
if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)):
    print(year, "is a leap year.")
else:
    print(year,"is not a leap year.")