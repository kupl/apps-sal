def snail(array):
    next_dir = {'right': 'down', 'down': 'left', 'left': 'up', 'up': 'right'}
    dir = 'right'
    snail = []
    while array:
        if dir == 'right':
            snail.extend(array.pop(0))
        elif dir == 'down':
            snail.extend([x.pop(-1) for x in array])
        elif dir == 'left':
            snail.extend(list(reversed(array.pop(-1))))
        elif dir == 'up':
            snail.extend([x.pop(0) for x in reversed(array)])
        dir = next_dir[dir]
    return snail
