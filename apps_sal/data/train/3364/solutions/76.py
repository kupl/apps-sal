from math import sqrt
def predict_age(*ages):
    result = []
    for n in ages:
        result.append(n*n)
    return sqrt(sum(result)) // 2
