def generate_number(squad, n):
    if n not in squad:
        return n
    print((squad, n))
    for i in range(0, 10):
        b = i * 10 + n - i if n - i < 10 and n - i > 0 else n
        if b not in squad:
            return b
    return None
