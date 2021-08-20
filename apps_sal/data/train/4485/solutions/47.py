def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return code
    elif code == '9':
        song = []
        a = 'bottles of beer'
        b = 'on the wall'
        c = '\nTake one down and pass it around'
        d = 'bottle of beer'
        for i in range(99, 2, -1):
            song.append(f'{i} {a} {b}, {i} {a}.{c}, {i - 1} {a} {b}.')
        song.append(f'2 {a} {b}, 2 {a}.{c}, 1 {d} {b}.')
        song.append(f'1 {d} {b}, 1 {d}.{c}, no more {a} {b}.\nNo more {a} {b}, no more {a}.')
        song.append(f'Go to the store and buy some more, 99 {a} {b}.')
        return '\n'.join(song)
