def predict_age(*argv):
    return sum(x * x for x in argv)**(1 / 2) // 2
