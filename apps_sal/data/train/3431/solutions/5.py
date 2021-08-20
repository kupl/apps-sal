def warn_the_sheep(queue):
    wolf_positon = 0
    for (postion, item) in enumerate(queue):
        if item == 'wolf':
            wolf_positon = postion + 1
        if wolf_positon == len(queue):
            return 'Pls go away and stop eating my sheep'
    return f'Oi! Sheep number {len(queue) - wolf_positon}! You are about to be eaten by a wolf!'
