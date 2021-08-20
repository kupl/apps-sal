def remove_chars(s):
    letters = 'abcdefghijklmnopqrstuvwxyz '
    return ''.join([i for i in s if i in letters or i in letters.upper()])
