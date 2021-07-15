def predict_age(*ages):
    return (sum(a**2 for a in ages) ** 0.5) // 2
