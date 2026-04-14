# BMI claculator 

weight=float(input("Enter the value:"))
height=float(input("Enter the value:"))

BMI= (weight)/(height**2)
print(f"Your BMI is {round(BMI,1)}")    #eg. 22.45 = 22.5

if BMI<18.5:
    print("Underweight 😞")
elif BMI < 25:
    print("Noral Weight 👍")
elif BMI < 30:
    print("Overweight 👎")
else:
    print("Obese")

