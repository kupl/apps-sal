from math import ceil
def cost(n):
    return 30 + [ceil((n-65)/30)*10, 0][n<60]
