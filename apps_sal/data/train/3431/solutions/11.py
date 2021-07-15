def warn_the_sheep(queue):
    count = 1
    wolf = 0
    for e in reversed(queue):
        count += 1
        if e == 'wolf':
            wolf = count - 2
            if wolf == 0:
                return 'Pls go away and stop eating my sheep'
    return f'Oi! Sheep number {wolf}! You are about to be eaten by a wolf!'
