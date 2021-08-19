while True:
    s = input()
    if s[0] == '#':
        break
    s = s.replace('%', '%25')
    s = s.replace(' ', '%20')
    s = s.replace('!', '%21')
    s = s.replace('$', '%24')
    s = s.replace('(', '%28')
    s = s.replace(')', '%29')
    s = s.replace('*', '%2a')
    print(s)
