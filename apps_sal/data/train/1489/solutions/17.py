# cook your dish here
try:
    s, k = map(int, input().split())
    num = str(s)
    l = []
    for i in range(len(num)):
        l.append(int(num[i]))
    cnt = 0
    for i in range(len(l)):
        if k == 0:
            break
        if l[i] != 9:
            l[i] = 9
            cnt += 1
        if cnt == k:
            break
    for i in l:
        print(i, end="")
    print()
except EOFError as e:
    pass
