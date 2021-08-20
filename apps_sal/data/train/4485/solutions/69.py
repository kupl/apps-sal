def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return code
    elif code == '9':
        text = '\n'.join((f'{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, {i - 1} bottles of beer on the wall.' for i in range(99, 2, -1)))
        text += '\n2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.'
        text += '\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.'
        text += '\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
        return text
    else:
        return None
