def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    if code == 'Q':
        return 'Q'
    if code == '9':
        out = '\n'.join(['{} bottles of beer on the wall, {} bottles of beer.\nTake one down and pass it around, {} bottles of beer on the wall.'.format(x + 1, x + 1, x) for x in range(98, 1, -1)])
        out += '\n2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n'
        out += '1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n'
        out += 'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
        return out
    return None
