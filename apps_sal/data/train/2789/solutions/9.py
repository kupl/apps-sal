def bmi(weight, height):
    BMI=weight/(height*height)
    return 'Underweight'if BMI<=18.5 else( 'Normal'if BMI<=25.0 else ('Overweight'if BMI<=30.0 else 'Obese'))
