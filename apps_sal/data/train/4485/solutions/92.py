def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return 'Q'
    elif code == '9':
        lyrics = ''
        for i in range(99, 2, -1):
            lyrics += '{bottles} bottles of beer on the wall, {bottles} bottles of beer.\n'.format(bottles=i)
            lyrics += 'Take one down and pass it around, {bottles} bottles of beer on the wall.\n'.format(bottles=i-1)
        lyrics += '2 bottles of beer on the wall, 2 bottles of beer.\n'
        lyrics += 'Take one down and pass it around, 1 bottle of beer on the wall.\n'
        lyrics += '1 bottle of beer on the wall, 1 bottle of beer.\n'
        lyrics += 'Take one down and pass it around, no more bottles of beer on the wall.\n'
        lyrics += 'No more bottles of beer on the wall, no more bottles of beer.\n'
        lyrics += 'Go to the store and buy some more, 99 bottles of beer on the wall.'
        return lyrics
    return None
