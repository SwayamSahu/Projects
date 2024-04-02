import math
def BMI_calc():
    ht = float(input("Enter your height in meters? "))
    wt = float(input("Enter your weight in kgs? "))

    BMI = wt/(ht*ht)

    print("Your BMI is: ",round(BMI,3))

    if BMI<18.5:
        print("Underweight")
    elif BMI>18.5 and BMI<=24.9:
        print("Normal weight")
    elif BMI>24.9 and BMI<=29.9:
        print("Overweight")
    else:
        print("Obesity")
BMI_calc()        
