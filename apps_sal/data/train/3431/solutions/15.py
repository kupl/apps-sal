def warn_the_sheep(q):
    pos = len(q) - 1 - q.index('wolf')
    return 'Pls go away and stop eating my sheep' if not pos else f'Oi! Sheep number {pos}! You are about to be eaten by a wolf!'
