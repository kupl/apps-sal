def camelize(str_):
    k = ''
    str_ = str_.lower()
    for x in str_:
        if x.isalnum():
            k += x
        else:
            k += ' '
    return ''.join((x.capitalize() for x in k.split()))
