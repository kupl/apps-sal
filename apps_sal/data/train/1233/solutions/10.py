def isgood(s):
    c = 0
    for i in set(s):
        k = s.count(i)
        if k % 2:
            c += 1
        if c == 2:
            return 0
    return 1


tc = int(input())
for i in range(tc):
    flag = 0
    s = input()
    n = len(s)
    g = n
    while g:
        for i in range(n - g + 1):
            if isgood(s[i:i + g]):
                print(g)
                flag = 1
                break
        g -= 1
        if flag:
            break
