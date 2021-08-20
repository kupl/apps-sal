def olympic_ring(string):
    n = sum((string.count(c) for c in 'ADOPQRabdegopq')) + string.count('B') * 2
    return ['Not even a medal!', 'Bronze!', 'Silver!', 'Gold!'][max(min(int(n / 2) - 1, 3), 0)]
