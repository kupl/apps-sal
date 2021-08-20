def warn_the_sheep(queue):
    N = queue[::-1].index('wolf')
    return 'Pls go away and stop eating my sheep' if queue[-1] == 'wolf' else f'Oi! Sheep number {N}! You are about to be eaten by a wolf!'
