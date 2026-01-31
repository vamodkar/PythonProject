weight = float(input("Enter weight in KG: "))
height = float(input("Enter height in feet: "))
height = height * 0.3048
bmi = weight / (height * height)

if bmi < 18.5:
    print(f"{bmi} : You are underweight.")
elif bmi >= 18.5 and bmi <= 25:
    print(f"{bmi} : You have a normal weight.")
elif bmi >= 25 and bmi <= 30:
    print(f"{bmi} : You are overweight.")
elif bmi >= 30:
    print(f"{bmi} : You are obese.")
else:
    print("You are clinically obese.")