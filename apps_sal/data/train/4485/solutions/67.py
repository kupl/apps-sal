def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return code
    elif code == '9':
        bottles = 99
        s = str(bottles) + ' bottles of beer on the wall, ' + str(bottles) + ' bottles of beer.\nTake one down and pass it around, ' + str(bottles - 1) + ' bottles of beer on the wall.\n'
        for i in range(bottles - 1, 2, -1):
            s += str(i) + ' bottles of beer on the wall, ' + str(i) + ' bottles of beer.\nTake one down and pass it around, ' + str(i - 1) + ' bottles of beer on the wall.\n'
        s += '2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, ' + str(bottles) + ' bottles of beer on the wall.'
        return s
    return None
