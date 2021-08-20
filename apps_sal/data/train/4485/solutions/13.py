def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return code
    elif code == '9':
        lyrics = ''
        for index in range(99, 0, -1):
            first = '%d %s' % (index, 'bottles' if index > 1 else 'bottle')
            next = '%s' % (str(index - 1) + ' bottles' if index > 2 else str(index - 1) + ' bottle' if index == 2 else 'no more bottles')
            lyrics += '%s of beer on the wall, %s of beer.\nTake one down and pass it around, %s of beer on the wall.\n' % (first, first, next)
        lyrics += 'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
        return lyrics
    else:
        return None
