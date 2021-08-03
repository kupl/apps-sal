def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    import math
    oldAge = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    newAge = []
    y = 0
    x = 0
    z = 0
    r = 0
    for i in range(0, len(oldAge)):
        newAge.append(oldAge[i] * oldAge[i])
    z = sum(newAge)
    y = math.sqrt(z)
    r = y / 2
    x = math.floor(r)
    print(x)
    return x
