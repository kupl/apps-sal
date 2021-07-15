def knight_rescue(N, x, y):
    even = (x + y) % 2 == 0
    for step in N:
        if step & 1 == 0 or even:
            return True
    return False
