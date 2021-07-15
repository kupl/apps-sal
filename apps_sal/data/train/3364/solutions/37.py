def predict_age(*xs):    
    return int(sum(map(lambda x : x**2, xs)) ** 0.5 / 2)
