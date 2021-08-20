def generate_number(squad, n):
    return n if n not in squad else None if n < 10 else next((x for x in range(10, 100) if sum((int(c) for c in str(x))) == n and x not in squad), None)
