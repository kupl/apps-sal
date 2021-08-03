def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    if code == 'Q':
        return code
    if code == '9':
        lyrics = ''
        for i in range(99, 0, -1):
            lyrics += '{} bottle{} of beer on the wall, {} bottle{} of beer.\n'.format(i, 's' if i > 1 else '', i, '' if i == 1 else 's')
            lyrics += 'Take one down and pass it around, {} bottle{} of beer on the wall.\n'.format(i - 1 if i > 1 else 'no more', '' if i == 2 else 's')
        lyrics += 'No more bottles of beer on the wall, no more bottles of beer.\n'
        lyrics += 'Go to the store and buy some more, 99 bottles of beer on the wall.'
        return lyrics
