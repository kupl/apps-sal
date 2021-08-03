def warn_the_sheep(queue):
    w = queue.index('wolf') + 1
    l = len(queue)

    if w == l:
        return 'Pls go away and stop eating my sheep'
    else:
        return f'Oi! Sheep number {l-w}! You are about to be eaten by a wolf!'
