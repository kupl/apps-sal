def predict_age(a1, a2, a3, a4, a5, a6, a7, a8):
    ages = [a1, a2, a3, a4, a5, a6, a7, a8]
    return sum([el ** 2 for el in ages]) ** 0.5 // 2
