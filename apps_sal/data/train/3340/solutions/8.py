import numpy as np
def sharkovsky(a, b):
    l = []
    for i in range(0, int(np.log2(max(a, b))) + 3):
        for j in range(3, max(a, b) + 1, 2):
            if a == (2 ** i) * j:
                l.append(a)
                a = b
                if len(l) >= 2:
                    return True
    for n in range(int(np.log2(max(a, b))) + 3, -1, -1):
        if a == 2 ** n:
            l.append(a)
            a = b
            if len(l) >= 2:
                return True
    return False
