def dashatize(n):
    if n == None:
        return 'None'
    s = ''
    n_s = str(n).strip('-')
    for c in n_s:
        if int(c) % 2 == 0:
            s += c
        else:
            s += '-' + c + '-'
    return s.replace('--', '-').strip('-')

