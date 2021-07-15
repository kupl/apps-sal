import math
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    lst = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    second = []
    summ = 0
    for age in lst:
        first = age*age
        second.append(first)
    for product in second:
        summ += product
    summ = math.sqrt(summ)
    answer = summ/2
    return int(answer)
