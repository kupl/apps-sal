def count_sheep(n):
    sheep = []
    for i in range(1, n + 1):
        sheep.append(f"{i} sheep...")

    return ''.join(sheep)
