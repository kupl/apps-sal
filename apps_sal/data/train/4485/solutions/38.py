def HQ9(code):
    s = ''''''
    x = 99
    if code == '9':
        while (x >= 0):
            if x - 1 == 0:
                s += f'''{str(x)} bottle of beer on the wall, {str(x)} bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.'''
                break
            if x > 1:
                s += f'''{str(x)} bottles of beer on the wall, {str(x)} bottles of beer.\n'''
                if x - 1 > 1:
                    s += f'''Take one down and pass it around, {str(x - 1)} bottles of beer on the wall.\n'''
                else:
                    s += f'''Take one down and pass it around, {str(x - 1)} bottle of beer on the wall.\n'''
            else:
                s += f'''{str(x)} bottle of beer on the wall, {str(x)} bottle of beer.
Take one down and pass it around, {str(x - 1)} bottle of beer on the wall.\n'''
            x -= 1
    return {'H': 'Hello World!', 'Q': 'Q', '9': s}.get(code)
