def knight_rescue(N, x, y):
    e = any((i % 2 == 0 for i in N))
    return e or (x + y) % 2 == 0
