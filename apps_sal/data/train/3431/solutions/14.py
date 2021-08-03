def warn_the_sheep(queue):
    wolf = queue.index('wolf') + 1
    length = len(queue)
    if wolf == length:
        return 'Pls go away and stop eating my sheep'
    else:
        return 'Oi! Sheep number ' + str(length - wolf) + '! You are about to be eaten by a wolf!'
