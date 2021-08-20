def gordon(a):
    (out, vowels) = ('', 'eiou')
    for i in a:
        if i == 'a':
            out += '@'
        elif i in vowels:
            out += '*'
        elif i == ' ':
            out += '!!!! '
        else:
            out += str(i).upper()
    return '%s!!!!' % out
