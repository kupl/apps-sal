def no_space(x):
    x = list(x)
    for i in range(len(x)):
        if x[i] == ' ':
            x.remove(x[i])
            x.append('')
    while x[-1] == '':
        x.pop()
    for i in range(len(x)):
        if x[i] == ' ':
            x.remove(x[i])
            x.append('')
    while x[-1] == '':
        x.pop()
    for i in range(len(x)):
        if x[i] == ' ':
            x.remove(x[i])
            x.append('')
    while x[-1] == '':
        x.pop()
    for i in range(len(x)):
        if x[i] == ' ':
            x.remove(x[i])
            x.append('')
    while x[-1] == '':
        x.pop()
    return ''.join(x)
