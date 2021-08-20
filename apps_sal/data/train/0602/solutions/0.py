m = 9999999
word = ''
p = ''
try:
    s = input().split()
    for i in s:
        if len(i) <= m:
            m = len(i)
            word = i
    p = word
    for i in s:
        p += ' ' + i + ' ' + word
    print(p)
except EOFError:
    pass
