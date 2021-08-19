def stringy(size):
    strng = ''
    if size % 2 == 1:
        for i in range((size + 1) // 2):
            strng += '10'
        return strng[:-1]
    else:
        for i in range(size // 2):
            strng += '10'
        return strng
