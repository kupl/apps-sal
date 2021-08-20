def warn_the_sheep(queue):
    p = queue[::-1].index('wolf')
    return f'Oi! Sheep number {p}! You are about to be eaten by a wolf!' if p != 0 else 'Pls go away and stop eating my sheep'
