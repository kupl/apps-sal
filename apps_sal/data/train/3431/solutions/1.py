def warn_the_sheep(queue):
    i = queue[::-1].index('wolf')
    if i == 0:
        return 'Pls go away and stop eating my sheep'
    return f'Oi! Sheep number {i}! You are about to be eaten by a wolf!'
