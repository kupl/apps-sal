import numpy as np

def cal_n_bug(x, y, z):
    a = np.array([[1,1,1], [8,6,6], [0,2,1]])
    b = np.array([x, y, z])
    s = np.linalg.solve(a, b)
    return list(map(int, s)) if all(x>=0 for x in s) else [-1, -1, -1]
