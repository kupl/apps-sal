def correct(string):
    s = ''
    for i in string:
        s = string.replace('5', 'S').replace('1', 'I').replace('0', 'O')
    return s
