def HQ9(code):
    bottles = 100
    res = ''
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return 'Q'
    elif code == '9':
        for i in range(99):
            if bottles == 3:
                res += '2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.'
                bottles -= 1
            elif bottles == 2:
                res += '\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.'
                res += '\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
            else:
                bottles -= 1
                res += '{} bottles of beer on the wall, {} bottles of beer.\nTake one down and pass it around, {} bottles of beer on the wall.\n'.format(bottles, bottles, bottles - 1)
        return res
