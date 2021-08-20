def uni_total(string):
    if string == '':
        return 0
    return sum((ord(i) for i in string))
