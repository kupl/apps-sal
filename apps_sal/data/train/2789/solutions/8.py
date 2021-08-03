def bmi(weight, height):
    result = weight / height / height
    return "Underweight Normal Overweight Obese".split()[
        (result > 18.5) +
            (result > 25.0) +
            (result > 30.0)]
