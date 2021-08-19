def predict_age(*args):
    return int(sum((n * n for n in args)) ** 0.5 // 2)
