t = int(input())
for _ in range(t):
    n = int(input())
    l1 = []
    if n == 1:
        print('*')
    elif n == 3:
        print('*')
        print('**')
        print('*')
    else:
        s1 = ""
        n1 = n // 2
        n1 += 1
        for i in range(1, n1 + 1):
            s1 = ""
            if i == 1:
                s1 += '*'
            elif i == 2:
                s1 += '**'
            else:
                s1 += '*'
                for j in range(2, i):
                    s1 += ' '
                s1 += '*'
            l1.append(s1)
    for i in l1:
        print(i)
    l1.reverse()
    for i in range(1, len(l1)):
        print(l1[i])
