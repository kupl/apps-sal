def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    if code == 'Q':
        return code
    if code == '9':
        line = ''
        for i in range(99, -1, -1):
            if i == 0:
                line += 'No more bottles of beer on the wall, no more bottles of beer.\n'
                line += 'Go to the store and buy some more, 99 bottles of beer on the wall.'
            elif i == 1:
                line += str(i) + ' bottle of beer on the wall, ' + str(i) + ' bottle of beer.\n'
                line += 'Take one down and pass it around, no more bottles of beer on the wall.\n'
            elif i == 2:
                line += str(i) + ' bottles of beer on the wall, ' + str(i) + ' bottles of beer.\n'
                line += 'Take one down and pass it around, ' + str(i - 1) + ' bottle of beer on the wall.\n'
            else:
                line += str(i) + ' bottles of beer on the wall, ' + str(i) + ' bottles of beer.\n'
                line += 'Take one down and pass it around, ' + str(i - 1) + ' bottles of beer on the wall.\n'     
        return line
    else:
        pass
