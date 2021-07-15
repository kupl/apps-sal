import math
def halving_sum(n):
    counter = 0
    div = n
    result = 0
    while div >= 1:
        div = math.floor(n/2**counter)
        counter += 1
        result += div
    return result
        

