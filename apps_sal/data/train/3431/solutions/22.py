def warn_the_sheep(queue):
    queue.reverse()
    if queue.index('wolf')==0:
        return 'Pls go away and stop eating my sheep'
    else:
       return 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(queue.index('wolf'))

