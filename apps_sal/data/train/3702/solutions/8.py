def olympic_ring(string):
    rings = 'abdegopqADOPQRBB'
    count = sum(string.count(c) for c in rings) // 2
    if count <= 1:
        return 'Not even a medal!'
    if count == 2:
        return 'Bronze!'
    if count == 3:
        return 'Silver!'
    return 'Gold!'
