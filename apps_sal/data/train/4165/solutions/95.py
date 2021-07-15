def uni_total(string):
    x = 0
    if string == '':
        return 0
    for i in range(len(string)):
        x += int(ord(string[i]))
    return x
