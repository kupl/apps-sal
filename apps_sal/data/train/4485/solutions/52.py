def HQ9(code):
    if code == 'H':
        return "Hello World!"
    elif code == 'Q':
        return code
    elif code == '9':
        return "\n".join([str(n) + " bottles of beer on the wall, " + str(n) + " bottles of beer.\nTake one down and pass it around, " + str(n - 1) + " bottles of beer on the wall." if n > 2 else "2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall." for n in range(99, 1, -1)])
    else:
        return None
