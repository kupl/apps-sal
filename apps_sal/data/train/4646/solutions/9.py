def encode(s):
    res = ''
    for i in range(len(s)):
        if s[i].isupper():
            if (ord(s[i]) - 65) % 2 == 0:
                res += '0'
            elif (ord(s[i]) - 65) % 2 == 1:
                res += '1'
        elif s[i].islower():
            if (ord(s[i]) - 97) % 2 == 0:
                res += '0'
            elif (ord(s[i]) - 97) % 2 == 1:
                res += '1'
        else:
            res += s[i]
    return res
