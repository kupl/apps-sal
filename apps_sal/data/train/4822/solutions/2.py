def mastermind(g):
    return map(g.check, map(list, __import__('itertools').permutations((c for c in ['Red', 'Blue', 'Green', 'Orange', 'Purple', 'Yellow'] for _ in range(g.check([c] * 4).count('Black'))))))
