def knight_rescue(N, x, y):
    return (x - y) % 2 == 0 or any((n % 2 == 0 for n in N))
