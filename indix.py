def classifybmi(bmi):
    "Classify BMI into categories."
    if bmi < 18.5: 
        return "Under weight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Over weight"
    else:
        return "Obese"


def calculatebmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)."""
    bmi = weight / (height ** 2)
    return bmi

def main():
    print("=== BMI Calculator ===")
    print("="*50)
    
    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))

        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive numbers.")
            return

        bmi = calculatebmi(weight, height)
        category = classifybmi(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"BMI Category: {category}")

    except ValueError:
        print("Invalid input! Please enter numeric values for weight and height.")
        
if __name__ == "__main__":
    main()
