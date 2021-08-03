def warn_the_sheep(queue):
    print(queue[-1])
    return ('Pls go away and stop eating my sheep', 'Oi! Sheep number {0}! You are about to be eaten by a wolf!'.format(len(queue[queue.index('wolf')::]) - 1))[queue[-1] == 'sheep']
