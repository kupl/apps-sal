def predict_age(*ages):
    return pow(sum((a * a for a in ages)), 0.5) // 2
