def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) based on weight (in kilograms) and height (in meters).
    """
    bmi = weight / (height ** 2)
    return bmi


def interpret_bmi(bmi):
    """
    Interpret the BMI value and provide a corresponding category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)

    print("BMI: {:.2f}".format(bmi))
    print("Category: {}".format(category))


if __name__ == "__main__":
    main()
