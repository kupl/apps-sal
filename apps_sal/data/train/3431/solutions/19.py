def warn_the_sheep(queue):
    if queue.index('wolf') == len(queue) - 1:
        return 'Pls go away and stop eating my sheep'
    else:
        sheep = queue[::-1].index('wolf')
        return f'Oi! Sheep number {sheep}! You are about to be eaten by a wolf!'
