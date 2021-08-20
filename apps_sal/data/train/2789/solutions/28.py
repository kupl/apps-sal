def bmi(weight, height):
    bm = weight / height ** 2.0
    for (val, outp) in zip([18.5, 25, 30], ['Underweight', 'Normal', 'Overweight']):
        if bm <= val:
            return outp
    return 'Obese'
