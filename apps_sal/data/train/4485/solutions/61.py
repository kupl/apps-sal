lyrics = '\n'.join((f"{i} bottle{('s' if i != 1 else '')} of beer on the wall, {i} bottle{('s' if i != 1 else '')} of beer.\nTake one down and pass it around, {(i - 1 if i != 1 else 'no more')} bottle{('s' if i != 2 else '')} of beer on the wall." for i in range(99, 0, -1)))
lyrics += '\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'


def HQ9(i):
    return {'H': 'Hello World!', 'Q': 'Q', '9': lyrics}.get(i)
