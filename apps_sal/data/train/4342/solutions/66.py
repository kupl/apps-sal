def no_space(x):
    line = ''
    for i in x.split(' '):
        line = line + i.strip()
    return line
