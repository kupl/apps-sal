def knight_rescue(N, x, y):
    return not ((x + y) % 2 and all((n % 2 for n in N)))
