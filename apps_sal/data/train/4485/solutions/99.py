def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    if code == 'Q':
        return 'Q'
    if code == '9':
        t = ''
        b = 99
        while b>2:
            t += str(b)+' bottles of beer on the wall, '+str(b)+' bottles of beer.\n'
            t += 'Take one down and pass it around, '+str(b-1)+' bottles of beer on the wall.\n'
            b -= 1
        t += '2 bottles of beer on the wall, 2 bottles of beer.\n'
        t += 'Take one down and pass it around, 1 bottle of beer on the wall.\n'
        t += '1 bottle of beer on the wall, 1 bottle of beer.\n'
        t += 'Take one down and pass it around, no more bottles of beer on the wall.\n'
        t += 'No more bottles of beer on the wall, no more bottles of beer.\n'
        t += 'Go to the store and buy some more, 99 bottles of beer on the wall.'
        return t
    else:
        return None
