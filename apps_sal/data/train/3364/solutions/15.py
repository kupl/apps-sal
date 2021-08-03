import math


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):

    list1 = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    list2 = []

    for x in list1:
        list2.append(x * x)

    list_sum = sum(list2)

    list_sum2 = math.sqrt(list_sum) / 2

    print(int(list_sum2))
    return int(list_sum2)


predict_age(65, 60, 75, 55, 60, 63, 64, 45)
