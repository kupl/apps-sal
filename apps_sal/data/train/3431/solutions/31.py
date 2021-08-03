def warn_the_sheep(queue):
    cnt = 1
    for i in range(len(queue) - 1, 0, -1):
        if queue[i] == 'wolf':
            return 'Pls go away and stop eating my sheep'
        elif queue[i] == 'sheep' and queue[i - 1] == 'wolf':
            return 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(cnt)
        cnt += 1
    return 'Pls go away and stop eating my sheep'
