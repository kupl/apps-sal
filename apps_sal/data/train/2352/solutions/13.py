def s():
    a = input()
    r = 'http://' if a[0] == 'h' else 'ftp://'
    if a[0] == 'h':
        a = a[4:]
    else:
        a = a[3:]
    c = a[0]
    a = a[1:].replace('ru', '.ru/', 1)
    print(r, c, a[:-1] if a[-1] == '/'else a, sep='')


s()
