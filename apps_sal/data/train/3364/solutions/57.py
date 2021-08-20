import math


def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    age_list = []
    squares = []
    age_list.append(age_1)
    age_list.append(age_2)
    age_list.append(age_3)
    age_list.append(age_4)
    age_list.append(age_5)
    age_list.append(age_6)
    age_list.append(age_7)
    age_list.append(age_8)
    for i in age_list:
        multiply = i ** 2
        squares.append(multiply)
    add = sum(squares)
    answer = math.sqrt(add) / 2
    round_answer = int(round(answer, 2))
    return round_answer
