def predict_age(*ages):
    return int(sum((age * age for age in ages)) ** 0.5 / 2)
