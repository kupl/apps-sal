def kebabize(string):
    result = ''
    for c in string:
        if c.isupper():
            if result is not '':
                result += '-{}'.format(c.lower())
            else:
                result += c.lower()
        if c.islower():
            result += c
    return result
