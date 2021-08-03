def generate_number(squad, n):
    candidates = [n] + [(n - d) * 10 + d for d in range(9, 0, -1)]

    for x in candidates:
        if x < 100 and x not in squad:
            return x
