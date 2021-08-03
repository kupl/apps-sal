def warn_the_sheep(queue):
    queue.reverse()
    wolfnum = queue.index("wolf")
    if wolfnum == 0:
        return "Pls go away and stop eating my sheep"
    else:
        return "Oi! Sheep number {0}! You are about to be eaten by a wolf!".format(wolfnum)
