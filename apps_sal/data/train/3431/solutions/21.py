def warn_the_sheep(queue):
    z = 0
    for i in queue:
        z += 1
        if i == 'wolf' and len(queue) - z != 0:
            return 'Oi! Sheep number ' + str(len(queue) - z) + '! You are about to be eaten by a wolf!'
    return 'Pls go away and stop eating my sheep'
