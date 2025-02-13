weight = int(input("Please input your weight in kg: "))
height = int(input("Please input your height in cm: "))
BMI =  (weight / (height * height)) * 10000

if BMI <= 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal weight")
elif  BMI >= 25 and BMI <= 29.9:
    print("Overweight")
else:
    print("Obesity")