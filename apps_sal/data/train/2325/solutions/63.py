S = input().strip()
T = input().strip()
N = int(input())


def parse(s):
    cums = [0]
    for c in s:
        cums.append(cums[-1] + (1 if c == 'A' else 2))
    return cums


cumS = parse(S)
cumT = parse(T)

#print(S, cumS)
#print(T, cumT)

for _ in range(N):
    a, b, c, d = map(int, input().split())
    a, b, c, d = a - 1, b - 1, c - 1, d - 1
    vS = (cumS[b + 1] - cumS[a]) % 3
    vT = (cumT[d + 1] - cumT[c]) % 3
    #print(a, b, c, d, vS, vT)
    print("YES" if vS == vT else "NO")
