def smash(words):
    new_str = ''
    for i in words:
        new_str = new_str + i + ' '
    return new_str[0:-1]
