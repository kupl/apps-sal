for i in range(int(input())):
    n = int(input())
    abc = list(map(int, input().split()))
    query = int(input())
    q = []
    for j in range(query):
        q.append(int(input()))
    z = 0
    p = 0
    s = 0
    wlist = [n]
    while p < 30:
        x = n / abc[z]
        x = str(x)
        if x[x.index(".") + 1] == "0":
            wlist.append(int(x[0]))
            n = int(x[0])
        else:
            wlist.append(int(x[x.index(".") + 1]))
            n = int(x[x.index(".") + 1])
        if n == 0:
            break
        z += 1
        p += 1
        if z > 2:
            z = 0
    n = 0
    while True:
        if wlist[n:n + 3] == wlist[n + 3:n + 6]:
            s = 0
            break
        n += 1
    # print(n, wlist)
    mlist = wlist[n:n + 3]
    if n >= 31:
        n = 0
        while True:
            if wlist[n:n + 6] == wlist[n + 6:n + 12]:
                s = 3
                break
            n += 1
        mlist = wlist[n:n + 6]
    if n >= 31:
        n = 0
        while True:
            if wlist[n:n + 9] == wlist[n + 9:n + 18]:
                s = 6
                break
            n += 1
        mlist = wlist[n:n + 9]
    # print(n, wlist)
    for j in range(len(q)):
        if q[j] > n - 1:
            x = q[j] - n
            y = x % 3
            if s == 3:
                y = x % 6
            if s == 6:
                y = x % 9
            print(mlist[y])
        else:
            print(wlist[q[j]])

