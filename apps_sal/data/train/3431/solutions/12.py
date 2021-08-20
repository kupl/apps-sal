def warn_the_sheep(queue):
    if queue[-1] == 'wolf':
        return 'Pls go away and stop eating my sheep'
    else:
        for i in range(len(queue)):
            if queue[len(queue) - i - 1] == 'wolf':
                return 'Oi! Sheep number ' + str(i) + '! You are about to be eaten by a wolf!'
