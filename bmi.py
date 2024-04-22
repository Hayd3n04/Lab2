def calculate_bmi(height, weight): 

    print("Height = " + str(height)) 
    print("Weight = " + str(weight)) 
    bmi = weight / (height *height)

    print("BMI = " + str(bmi))

calculate_bmi(weight=57, height=1.73)   

def interpret_bmi(bmi) :
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 25:
        return "Normal weight"
    elif 25 <= bmi:
        return "Overweight"
    print("Your BMI is:", bmi)
    print("You are:", interpret_bmi(bmi))