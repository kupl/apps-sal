def olympic_ring(string):
    s = sum(2 if c == 'B' else 1 if c in 'abdegopqADOPQR' else 0 for c in string) // 2
    return 'Not even a medal!' if s <= 1 else 'Bronze!' if s == 2 else 'Silver!' if s == 3 else "Gold!"
