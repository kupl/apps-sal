for i in range(eval(input())):
    n = eval(input())
    w = input().split()
    q = []
    q.append(w[0])
    p = q[0]
    l = len(p)
    for j in range(l - 1, 0, -1):
        for k in range(0, l - j + 1):
            q.append(p[k:k + j])
    ans = []
    l = 0
    for j in q:
        ct = 0
        if(l > len(j)):
            break

        for k in w:
            if(k.find(j) != -1):
                ct += 1

        if(ct == n):
            ans.append(j)
            l = len(j)

    print(min(ans))
