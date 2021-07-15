import sys
readline = sys.stdin.readline

popcntsum = ((1<<1024) - 1)
Fa = [0] + [popcntsum//((1<<(1<<(i-1)))+1) for i in range(1,11)]
Fb = [0] + [Fa[i]<<(1<<(i-1)) for i in range(1,11)]
fila1 = Fa[1]
filb1 = Fb[1]
fila2 = Fa[2]
filb2 = Fb[2]
fila3 = Fa[3]
filb3 = Fb[3]
fila4 = Fa[4]
filb4 = Fb[4]
fila5 = Fa[5]
filb5 = Fb[5]
fila6 = Fa[6]
filb6 = Fb[6]
fila7 = Fa[7]
filb7 = Fb[7]
fila8 = Fa[8]
filb8 = Fb[8]
fila9 = Fa[9]
filb9 = Fb[9]
fila10 = Fa[10]
filb10 = Fb[10]
def popcount(x):
    x = (x&fila1) + ((x&filb1)>>1)
    x = (x&fila2) + ((x&filb2)>>2)
    x = (x&fila3) + ((x&filb3)>>4)
    x = (x&fila4) + ((x&filb4)>>8)
    x = (x&fila5) + ((x&filb5)>>16)
    x = (x&fila6) + ((x&filb6)>>32)
    x = (x&fila7) + ((x&filb7)>>64)
    x = (x&fila8) + ((x&filb8)>>128)
    x = (x&fila9) + ((x&filb9)>>256)
    x = (x&fila10) + ((x&filb10)>>512)
    return x


def check(S):
    if S == 0:
        return []
    if S < 0:
        return None
    G1 = [G[i]&S for i in range(N)]
    M = popcount(S)
    if M**2 == sum(G1[i] for i in range(N) if S&(1<<i)):
        return [(0, 1)]*M
    st = 0
    A = 0
    for i in range(N):
        if (1<<i) & S:
            st = i
            A = 1<<i
            break
    B = 0
    for i in range(N):
        if not (1<<i) & S:
            continue
        if not (G[st] & (1<<i)):
            B = 1<<i
            break
    T = (((1<<N)-1)^S)|A|B
    na = 1
    nb = popcount(B)
    T2 = None
    while T2 != T:
        T2 = T
        for i in range(N):
            if (1<<i) & T:
                continue
            fa = (na == popcount(G1[i]&A))
            fb = (nb == popcount(G1[i]&B))
            if fa and fb:
                continue
            if fa:
                A |= 1<<i
                T |= 1<<i
                na += 1
                continue
            if fb:
                B |= 1<<i
                T |= 1<<i
                nb += 1
                continue
            return None
    S2 = ((1<<N)-1) ^ T
    
    if na > nb:
        na, nb = nb, na
    ss = check(S2)
    if ss is None:
        return None
    return ss + [(na, nb)] 


N, M = map(int, readline().split())
G = [1<<i for i in range(N)]
for _ in range(M):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    G[a] |= 1<<b
    G[b] |= 1<<a
ss = check((1<<N)-1)
if ss is None:
    print(-1)
else:
    SA, SB = list(map(list, zip(*ss)))
    res = 1
    for sa, sb in zip(SA, SB):
        res = (res<<sa)|(res<<sb)
    ans = 10**9+7
    for i in range(N+1):
        if not (1<<i)&res:
            continue
        ans = min(ans, (i-1)*i//2 + (N-i-1)*(N-i)//2)
    print(ans)
