def knight_rescue(N, x, y):
    if x % 2 == 0 and y % 2 == 0:
        return True if any([i % 2 != 0 for i in N]) else (True if all([i % 2 == 0 for i in N]) else False)
    elif x % 2 != 0 and y % 2 != 0:
        return True if all([i % 2 != 0 for i in N]) else (True if any([i % 2 == 0 for i in N]) else False)
    return True if any([i % 2 == 0 for i in N]) else False
