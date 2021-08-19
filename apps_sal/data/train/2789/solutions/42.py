def bmi(weight, height):
    bo_m_i = weight / height ** 2
    if bo_m_i <= 18.5:
        return 'Underweight'
    elif bo_m_i <= 25.0:
        return 'Normal'
    elif bo_m_i <= 30.0:
        return 'Overweight'
    else:
        return 'Obese'
