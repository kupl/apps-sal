def predict_age(*args):
    sum = 0
    for i in args:
        sum += i*i
    return sum ** 0.5 // 2
