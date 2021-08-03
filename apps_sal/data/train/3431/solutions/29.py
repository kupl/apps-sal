def warn_the_sheep(queue):
    x = 0
    for i in queue:
        x = x + 1
        if i == 'wolf':
            b = len(queue) - x
            if b == 0:
                return 'Pls go away and stop eating my sheep'
            else:
                return "Oi! Sheep number {}! You are about to be eaten by a wolf!".format(b)
