(a, b) = [int(_) for _ in input().split()]
if b == 0:
    print(a)
else:
    l = []
    a = str(a)
    for i in range(len(a)):
        l.append(a[i])
    for i in range(len(l)):
        if b == 0:
            break
        if l[i] == '9':
            continue
        else:
            l[i] = '9'
            b -= 1
    s = ''
    for i in l:
        s += i
    print(s)
