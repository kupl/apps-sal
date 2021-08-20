def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == 'Q':
        return code
    elif code == '9':
        i = 99
        song = ''
        while i > 2:
            song += f'{str(int(float(i)))} bottles of beer on the wall, {str(int(float(i)))} bottles of beer.\nTake one down and pass it around, {str(int(float(i - 1)))} bottles of beer on the wall.\n'
            i -= 1
        return f'{song}2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
