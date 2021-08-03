def knight_rescue(N, x, y):
    for n in N:
        if n % 2 == 0:
            return True
    return (x + y) % 2 == 0
