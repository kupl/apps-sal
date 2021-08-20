def correct(string):
    chars = ['5', '0', '1']
    for ch in chars:
        return string.replace(chars[0], 'S').replace(chars[1], 'O').replace(chars[2], 'I')
