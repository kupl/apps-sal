def generate_number(squad, n):
    if n not in squad:
        return n
    for i in range(n - 9, 10):
        d = int(f"{i}{n-i}")
        if d not in squad and (n - i) > 0:
            return d
