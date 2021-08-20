def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return 'Q'
    elif code == '9':
        result = ''
        for i in range(99, 2, -1):
            iStr = str(i)
            result += iStr + ' bottles of beer on the wall, ' + iStr + ' bottles of beer.\n'
            result += 'Take one down and pass it around, ' + str(i - 1) + ' bottles of beer on the wall.\n'
        result += '2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n'
        result += '1 bottle of beer on the wall, 1 bottle of beer.\n'
        result += 'Take one down and pass it around, no more bottles of beer on the wall.\n'
        result += 'No more bottles of beer on the wall, no more bottles of beer.\n'
        result += 'Go to the store and buy some more, 99 bottles of beer on the wall.'
        return result


print(HQ9('Q'))
print(HQ9('H'))
print(HQ9('A'))
print(HQ9('9'))
