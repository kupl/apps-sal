def predict_age(*age):
    lt = [i * i for i in age]
    return int((sum(lt)**0.5) / 2)
