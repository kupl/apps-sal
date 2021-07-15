def warn_the_sheep(queue):
    p = queue.index('wolf')
    if p == len(queue) - 1:
        return "Pls go away and stop eating my sheep"
    else:
        return "Oi! Sheep number " + str(len(queue) - 1 - p) + "! You are about to be eaten by a wolf!"
