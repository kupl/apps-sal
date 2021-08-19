def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    if code == 'Q':
        return code
    if code == '9':
        text = f'99 bottles of beer on the wall, 99 bottles of beer.\nTake one down and pass it around, '
        for i in range(98, 1, -1):
            text += f'{i} bottles of beer on the wall.\n{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, '
        text += f'1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
        return text
