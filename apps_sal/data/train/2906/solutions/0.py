def generate_number(squad, n):
    if n not in squad:
        return n
    for i in range(1, 10):
        for j in range(1, 10):
            if i + j == n and i * 10 + j not in squad:
                return i * 10 + j
