def increment_string(strng):
    list1 = ''
    i = 0
    length = len(strng)
    if strng == '':
        return '1'
    if strng[-1].isdigit():
        i += 1
        while(i < length and strng[-i].isdigit()):
            i += 1
    else:
        return strng + '1'
    i -= 1
    number_string = str(int(strng[-i:]) + 1)
    return strng[:-i] + '0' * (i - len(number_string)) + number_string
