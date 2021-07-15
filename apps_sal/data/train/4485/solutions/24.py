def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return 'Q'
    elif code == '9':
        text = ''
        bottles = 99
        for i in range(bottles,0,-1):
            word = 'bottle'if i == 1 else 'bottles'
            if i > 1:
                s = f'{i} {word} of beer on the wall, {i} {word} of beer.\n'
                word = 'bottle'if i-1 == 1 else 'bottles'
                s += f'Take one down and pass it around, {i-1} {word} of beer on the wall.\n'
            else:
                s = f'{i} bottle of beer on the wall, {i} bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
            text += s
        return text
