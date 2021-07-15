import numpy as np
def regressionLine(x, y):
    b, a =  tuple(np.round(np.polyfit(x, y, 1), 4))
    return a, b

