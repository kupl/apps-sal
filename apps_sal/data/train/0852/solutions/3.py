t = int(input())
for _ in range(t):
    n = int(input())
    s = ""
    for i in range(1, n + 1):
        if i % 2 != 0:
            s += '1'
        else:
            s += '0'
    s1 = ''
    for i in range(1, n + 1):
        if i % 2 == 0:
            s1 += '1'
        else:
            s1 += '0'
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(s)
        else:
            print(s1)
