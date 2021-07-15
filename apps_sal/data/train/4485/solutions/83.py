def HQ9(code, number=99):
    if code == 'H':
        return 'Hello World!'
    elif code== 'Q':
        return 'Q'
    elif code== '9':
        if number == 1:
            return '1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
        elif number == 2:
            return '2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n'+ HQ9(code, number-1)
        elif number >= 3:
            return str(number)+' bottles of beer on the wall, '+str(number)+' bottles of beer.\nTake one down and pass it around, '+str(number-1)+' bottles of beer on the wall.\n'+ HQ9(code, number-1)
    return
