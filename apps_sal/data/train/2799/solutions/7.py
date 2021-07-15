def beasts(heads, tails):
    for orthus in range(heads//2 + 1):
        if orthus * 2 + (tails - orthus) * 5 == heads:
             return [orthus, tails - orthus]
    return 'No solutions'
