def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return 'Q'

    elif code == '9':
        text = ''
        for x in range(99, 1, -1):
            text += '{} bottles of beer on the wall, {} bottles of beer.\n'.format(x, x)
            if (x - 1 > 1):
                text += 'Take one down and pass it around, {} bottles of beer on the wall.\n'.format(x - 1)
            else:
                text += 'Take one down and pass it around, {} bottle of beer on the wall.\n'.format(x - 1)
        text += '1 bottle of beer on the wall, 1 bottle of beer.\n'
        text += 'Take one down and pass it around, no more bottles of beer on the wall.\n'

        text += 'No more bottles of beer on the wall, no more bottles of beer.\n'
        text += 'Go to the store and buy some more, 99 bottles of beer on the wall.'
        return text
    else:
        return None
