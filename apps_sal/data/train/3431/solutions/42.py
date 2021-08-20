def warn_the_sheep(queue):
    x = len(queue)
    z = 0
    for k in range(0, x):
        if queue[k] == 'wolf' and k < x:
            z += k
        else:
            z += 0
    j = x - z - 1
    if z >= x and j <= 0:
        return 'Pls go away and stop eating my sheep'
    elif j == 0:
        return 'Pls go away and stop eating my sheep'
    else:
        return 'Oi! Sheep number ' + str(j) + '! You are about to be eaten by a wolf!'
