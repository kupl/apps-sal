a = int(input())
while a:
    a = a - 1
    b = input()
    c = input()
    p = []
    for i in c:
        if i not in p:
            p.append(i)
    f = 0
    for i in b:
        if i not in p:
            continue
        else:
            f = 1
            break
    if f == 1:
        print('Yes')
    else:
        print('No')
