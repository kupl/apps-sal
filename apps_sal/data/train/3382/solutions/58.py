def lowercase_count(strng):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return len([i for i in strng if i in letters])
