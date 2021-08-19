def bmi(weight, height):
    scale = {18.5: 'Underweight', 25.0: 'Normal', 30.0: 'Overweight'}
    x = weight / height / height
    for (bmi_class, label) in scale.items():
        if x < bmi_class:
            return label
    return 'Obese'
