def predict_age(*args):
    result = 0
    for el in args:
        result += (el * el)
    return result**(1 / 2) // 2
