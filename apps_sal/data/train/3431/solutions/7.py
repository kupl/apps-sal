def warn_the_sheep(queue):
    pos = queue[::-1].index('wolf')
    if pos > 0:
        return 'Oi! Sheep number %s! You are about to be eaten by a wolf!' % pos
    return 'Pls go away and stop eating my sheep'
