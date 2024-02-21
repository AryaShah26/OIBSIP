def get_user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_bmi(weight, height):
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return None  # Handle the case where height is entered as 0

def classify_bmi(bmi):
    if bmi is None:
        return "Invalid input"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")

    weight = get_user_input("Enter your weight in kilograms: ")
    height = get_user_input("Enter your height in meters: ")

    bmi = calculate_bmi(weight, height)
    bmi_category = classify_bmi(bmi)

    print("\nResults:")
    if bmi is not None:
        print(f"Your BMI is: {bmi:.2f}")
        print(f"BMI Category: {bmi_category}")
    else:
        print("Error: Please make sure your height is not zero.")

if __name__ == "__main__":
    main()

