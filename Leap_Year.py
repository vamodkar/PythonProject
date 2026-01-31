year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} : You are a not leap year.")
        if year % 400 == 0:
            print(f"{year} : You are a leap year.")
else: print(f"{year} : You are not a leap year.")