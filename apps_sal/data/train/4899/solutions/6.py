i0 = 0.14849853757254047
from math import exp

def weight(n, w):
    area = i0 * sum([exp(-2*m) for m in range(n)])
    return w*area
