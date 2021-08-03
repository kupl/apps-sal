def knight_rescue(N, x, y):
    return not all(n & 1 and (x + y) & 1 for n in N)
