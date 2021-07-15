S = input()
T = input()
q = int(input())
abcd = [[int(i) for i in input().split()] for _ in range(q)]

sdp = [(0, 0)]
tdp = [(0, 0)]
for s in S :
    a, b = sdp[-1]
    if s == 'A' :
        sdp.append((a + 1, b))
    else :
        sdp.append((a, b + 1))
for t in T :
    a, b = tdp[-1]
    if t == 'A' :
        tdp.append((a + 1, b))
    else :
        tdp.append((a, b + 1))

for a, b, c, d in abcd :
    sa = sdp[b][0] - sdp[a-1][0]
    sb = sdp[b][1] - sdp[a-1][1]
    ta = tdp[d][0] - tdp[c-1][0]
    tb = tdp[d][1] - tdp[c-1][1]
    
    tb -= ta - sa
    if abs(sb - tb) % 3 == 0 :
        print('YES')
    else :
        print('NO')
