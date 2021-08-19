def warn_the_sheep(queue):
    return 'Oi! Sheep number ' + str(len(queue) - queue.index('wolf') - 1) + '! You are about to be eaten by a wolf!' if queue[-1] == 'sheep' else 'Pls go away and stop eating my sheep'
