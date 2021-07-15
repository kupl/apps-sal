import math
def aks_test(p):
    center = (math.factorial(p//2)*math.factorial(p-p//2))
    if center%p==0:
        return False
    return True
