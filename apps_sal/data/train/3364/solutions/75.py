def predict_age(*ages):
    return int(sum(i * i for i in ages) ** 0.5 / 2)
