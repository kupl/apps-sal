def bmi(weight, height):
    BMI = weight/height**2
    if (int(BMI) < 18.5):
        results = 'Underweight'
    elif (int(BMI) < 25.0 ):
        results = 'Normal'
    elif (int(BMI) < 30.0 ):
       results = 'Overweight'
    else:
        results ='Obese'
    return(results)
