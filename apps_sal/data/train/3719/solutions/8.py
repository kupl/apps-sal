import numpy as np
from sklearn.linear_model import LinearRegression

def starting_mark(h):
    
    X, Y = np.array([1.52, 1.83]).reshape(-1, 1), np.array([9.45, 10.67])
    model = LinearRegression().fit(X, Y)
    theta0 = model.intercept_
    theta1 = model.coef_
    
    return round(theta0.item() +theta1.item() *h, 2)


