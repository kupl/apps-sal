def warn_the_sheep(queue):
    if queue[-1] == 'wolf':
        return 'Pls go away and stop eating my sheep'
    position = len(queue) - queue.index('wolf') - 1
    return 'Oi! Sheep number ' + str(position) + '! You are about to be eaten by a wolf!'
