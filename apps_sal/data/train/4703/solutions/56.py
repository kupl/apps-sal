import numpy as np
def bar_triang(pointA, pointB, pointC):
    x0 = np.around((pointA[0] + pointB[0] + pointC[0]) / 3, decimals=4)
    y0 = np.around((pointA[1] + pointB[1] + pointC[1]) / 3, decimals=4) 
    return [x0, y0]
