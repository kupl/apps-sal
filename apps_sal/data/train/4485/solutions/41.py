def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return code
    elif code == '9':
        r = []
        for i in range(99, 1, -1):
            r.append('{} bottles of beer on the wall, {} bottles of beer.'.format(i, i))
            if i == 2:
                r.append('Take one down and pass it around, {} bottle of beer on the wall.'.format(i - 1))
            else:
                r.append('Take one down and pass it around, {} bottles of beer on the wall.'.format(i - 1))
        r.append('{} bottle of beer on the wall, {} bottle of beer.'.format(1, 1))
        r.append('Take one down and pass it around, no more bottles of beer on the wall.')
        r.append('No more bottles of beer on the wall, no more bottles of beer.')
        r.append('Go to the store and buy some more, 99 bottles of beer on the wall.')
        return '\n'.join(r)
