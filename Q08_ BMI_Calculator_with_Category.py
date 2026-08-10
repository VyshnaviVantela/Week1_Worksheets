def calculate_bmi(weight_kg, height_m):
    BMI = round((weight_kg / (height_m**2)),2)
    if BMI <18.5:
       category = 'Underweight'
    elif BMI > 18.5 and BMI < 24.9:
       category = 'Normal Weight'
    elif BMI > 25 and BMI < 29.9:
       category = 'Overweight'
    else:
       category = 'Obese'

    return {'bmi': BMI, 'category': category}

print(calculate_bmi(70, 1.75))
print(calculate_bmi(90, 1.75))
print(calculate_bmi(100, 1.75))


       
