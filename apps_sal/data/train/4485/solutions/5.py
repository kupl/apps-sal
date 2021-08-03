def HQ9(code):
    lyrics = '99 bottles of beer on the wall, 99 bottles of beer.\n'
    for i in range(98, 1, -1):
        lyrics += 'Take one down and pass it around, {} bottles of beer on the wall.\n'.format(i)
        lyrics += '{} bottles of beer on the wall, {} bottles of beer.\n'.format(i, i)
    lyrics += 'Take one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'

    mapper = {'H': 'Hello World!', 'Q': code, '9': lyrics}

    return mapper.get(code, None)
