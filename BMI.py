import sys
import math

def main():
    print("BMI Calculator")
    print("==============")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print("\nBMI Result:")
    print("-----------")
    print(f"Your BMI is: {bmi:.2f}")
    print("BMI Category:", category)

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
if __name__ == "__main__":
    main()
