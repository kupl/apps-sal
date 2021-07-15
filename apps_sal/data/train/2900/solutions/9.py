def string_transformer(s):
    str1 = ''.join([i.upper() if i.islower() else i.lower() for i in s])
    str2 = str1.split(' ')
    str2.reverse()
    return ' '.join(str2)
