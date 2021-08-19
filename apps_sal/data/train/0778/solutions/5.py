a = int(input(''))
l = []
for m in range(a):
    b = input('')
    l.append(b)
for m in range(a):
    n = list(l[m])
    n.reverse()
    s = ''
    for t in n:
        s = s + t
    w = int(s)
    print(w)
