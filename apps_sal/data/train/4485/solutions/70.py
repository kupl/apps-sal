def HQ9(code):
    count = 99
    second_count = count - 1
    song = ''
    two_left = '2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n'
    one_left = '1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n'
    none_left = 'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
    if code == 'H':
        return 'Hello World!'
    if code == 'Q':
        return code
    if code == '9':
        while count > 2:
            song = song + str(count) + ' bottles of beer on the wall, ' + str(count) + ' bottles of beer.\nTake one down and pass it around, ' + str(count - 1) + ' bottles of beer on the wall.\n'
            count -= 1
            if count == 2:
                song = song + two_left + one_left + none_left
        return song
    else:
        return None
