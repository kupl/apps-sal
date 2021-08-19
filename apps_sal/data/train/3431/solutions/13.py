def warn_the_sheep(queue):
    index = len(queue) - queue.index('wolf') - 1
    if index == 0:
        return 'Pls go away and stop eating my sheep'
    else:
        return 'Oi! Sheep number ' + str(index) + '! You are about to be eaten by a wolf!'
