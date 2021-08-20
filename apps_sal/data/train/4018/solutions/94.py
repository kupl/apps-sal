def isDigit(string):
    numbers = '-0123456789.'
    str_num = ''
    if string.strip() == '':
        return False
    else:
        x = string.strip()
        y = x[0]
        for (i, char) in enumerate(x):
            if char in numbers:
                if y == '-' and char == x[0]:
                    str_num += char
                elif x[i] == 0 or char != '-':
                    str_num += char
                else:
                    return False
            else:
                return False
        return True
