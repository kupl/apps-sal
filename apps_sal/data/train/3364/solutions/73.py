def predict_age(*ages):
    return pow(sum(a*a for a in ages), .5) // 2
