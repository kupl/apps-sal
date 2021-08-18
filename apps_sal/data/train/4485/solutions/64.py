def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    if code == 'Q':
        return 'Q'
    if code == '9':
        l = []
        for i in range(99, 0, -1):
            s = '{} bottle{} of beer on the wall, {} {} of beer.'.format(i, 's' if i != 1 else '', i, 'bottle' if i == 1 else 'bottles')
            l.append(s)
            s = 'Take one down and pass it around, {} {} of beer on the wall.'.format(i - 1 if (i - 1) != 0 else '', 'bottle' if i == 2 else ('bottles' if i != 1 else ''))
            l.append(s)
        l.append('No more bottles of beer on the wall, no more bottles of beer.')
        l.append('Go to the store and buy some more, 99 bottles of beer on the wall.')
        s = '\n'.join(l)
        s = s.replace('  of beer', 'no more bottles of beer')
        return s
