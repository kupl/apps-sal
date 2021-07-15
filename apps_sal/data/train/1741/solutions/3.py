MOD = 12345787
MSK = 1 << 5
ANS = [1]
FLAG = False

def trans(T, x):
    y = [0 for i in range(MSK)]
    for i in range(MSK):
        for j in T[i]:
            y[j] += x[i]
    for i in range(MSK):
        y[i] %= MOD
    return y

def prework(MAXN=10010):
    nonlocal FLAG
    if FLAG:
        return
    FLAG = True
    T = [[] for i in range(MSK)]
    for i in range(MSK):
        for j in range(MSK):
            if (i & j) == 0:
                rm = (MSK - 1) ^ (i | j)
                p = [k for k in range(5) if ((rm >> k) & 1) == 1]
                flag = (len(p) % 2 == 0)
                if flag:
                    for k in range(len(p) // 2):
                        flag &= (p[2 * k] + 1 == p[2 * k + 1])
                if flag:
                    T[i].append(j)
    x = [0 for i in range(MSK)]
    x[0] = 1
    nonlocal ANS
    for i in range(2 * MAXN):
        x = trans(T, x)
        if i % 2 == 1:
            ANS.append(x[0])

def five_by_2n(n):
    prework()
    nonlocal ANS
    return ANS[n]
