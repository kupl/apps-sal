def HQ9(code):
    x = ''
    bottles = 99
    while bottles > 2:
        x += '%d bottles of beer on the wall, %d bottles of beer.\n' % (bottles, bottles)
        x += 'Take one down and pass it around, %d bottles of beer on the wall.\n' % (bottles - 1)
        bottles -= 1
    x += '2 bottles of beer on the wall, 2 bottles of beer.\n' + 'Take one down and pass it around, 1 bottle of beer on the wall.\n' + '1 bottle of beer on the wall, 1 bottle of beer.\n' + 'Take one down and pass it around, no more bottles of beer on the wall.\n' + 'No more bottles of beer on the wall, no more bottles of beer.\n' + 'Go to the store and buy some more, 99 bottles of beer on the wall.'
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return 'Q'
    elif code == '9':
        return x
    else:
        return None
