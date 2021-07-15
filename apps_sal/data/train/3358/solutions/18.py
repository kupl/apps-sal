def correct(s):
    return ''.join('S' if x == '5' else 'O' if x == '0' else 'I' if x == '1' else x for x in s)
