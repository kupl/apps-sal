def camel_case(string):
    a = list(string)
    for i in range(0, len(a)):
        if i == 0 or a[i - 1] == ' ':
            a[i] = a[i].upper()
    return ''.join(a).replace(' ', '')
