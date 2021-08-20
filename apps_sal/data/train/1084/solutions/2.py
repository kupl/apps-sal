try:
    s = input()
    c = 0
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            c = c + 1
    if s[-1] == '1':
        print(c + 1)
    else:
        print(c)
except:
    pass
