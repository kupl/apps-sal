S = input()
T = input()
Q = int(input())
ABCD = [tuple(map(int,input().split())) for i in range(Q)]

csa = [0]
csb = [0]
for c in S:
    csa.append(csa[-1] + (c=='A'))
    csb.append(csb[-1] + (c=='B'))
cta = [0]
ctb = [0]
for c in T:
    cta.append(cta[-1] + (c=='A'))
    ctb.append(ctb[-1] + (c=='B'))

ans = []
for a,b,c,d in ABCD:
    a -= 1
    c -= 1
    sa = csa[b] - csa[a]
    sb = csb[b] - csb[a]
    ta = cta[d] - cta[c]
    tb = ctb[d] - ctb[c]
    s = (sb-sa)%3
    t = (tb-ta)%3
    ans.append('YES' if s==t else 'NO')
print(*ans, sep='\n')
