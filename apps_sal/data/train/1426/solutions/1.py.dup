t = int(input())
for i in range(t):
    n, m = list(map(int, input().split()))
    l = [0] + list(map(int, input().split()))
    s = 0
    c = 1
    m1 = []
    for i in range(n):
        d, f, b = list(map(int, input().split()))
        if(l[d] > 0):
            m1.append(d)
            s += f
            l[d] -= 1
        else:
            m1.append(0)
            s += b
    for i in range(n):
        if(m1[i] == 0):
            for j in range(c, m + 1):
                if(l[j] > 0):
                    m1[i] = j
                    l[j] -= 1
                    c = j
                    break
    print(s)
    print(*m1)
