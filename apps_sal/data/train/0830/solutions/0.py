for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    l = []
    flag = 0
    for i in range(n):
        if b[i] != a[i]:
            if b[i] in a and b[i] < a[i]:
                l.append(b[i])
            else:
                flag = 1
                break
    if flag == 1:
        print(-1)
    elif l == []:
        print(0)
    else:
        l = sorted(list(set(l)), reverse=True)
        print(len(l))
        for i in range(len(l)):
            q = []
            r = []
            for j in range(len(a)):
                if l[i] == b[j]:
                    q.append(j)
                    r.append(a[j])
            if l[i] not in r:
                for k in range(len(a)):
                    if a[k] == l[i]:
                        q.append(k)
            print(len(q), *q)
