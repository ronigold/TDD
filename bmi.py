def bmi(weight, height):
    return round((weight/height**2),2)

def bmi_categories(weight, height):
    if bmi(weight, height) < 15:
        return 'Very severely underweight'
    elif bmi(weight, height) < 16:
        return 'Severely underweight'
    elif bmi(weight, height) < 18.5:
        return 'Underweight'
    elif bmi(weight, height) < 25:
        return 'Normal (healthy weight)'
    elif bmi(weight, height) < 30:
        return 'Overweight'
    elif bmi(weight, height) < 35:
        return 'Obese Class I (Moderately obese)'
    elif bmi(weight, height) < 40:
        return 'Obese Class II (Severely obese)'
    elif bmi(weight, height) < 45:
        return 'Obese Class III (Very severely obese)'
    elif bmi(weight, height) < 50:
        return 'Obese Class IV (Morbidly obese)'
    elif bmi(weight, height) < 60:
        return 'Obese Class V (Super obese)'
    elif bmi(weight, height) >= 60:
        return 'Obese Class VI (Hyper obese)'