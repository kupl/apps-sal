for a0 in range(int(input())):
    n = int(input())
    l = []
    for i in range(1, n + 1):
        l.append(str(i))
    l = l[::-1]
    s = ""
    for i in l:
        s += i
    print(s)
    i = 0
    while len(set(l)) > 2 or "2" in l:
        l[i] = "*"
        s = ""
        for j in l:
            s += j
        print(s)

        i += 1
