def generate_number(squad, n):
    if n not in squad:
        return n
    for i in range(1, 10):
        for j in range(1, 10):
            if i + j == n:
                x = int(f'{i}{j}')
                if x not in squad:
                    return x
