def warn_the_sheep(queue):
    if queue[-1] == 'wolf':
        return 'Pls go away and stop eating my sheep'  
    else: 
        return 'Oi! Sheep number ' + str(len(queue) - queue.index('wolf') -1) + '! You are about to be eaten by a wolf!'
