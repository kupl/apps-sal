
import sys
readline = sys.stdin.readline
S = readline().rstrip()
T = readline().rstrip()
q = int(readline())

Sa = [0] * (len(S) + 1)
Sb = [0] * (len(S) + 1)
Ta = [0] * (len(T) + 1)
Tb = [0] * (len(T) + 1)

for i in range(len(S)):
    if S[i] == "A":
        Sa[i + 1] = 1
    else:
        Sb[i + 1] = 1
for i in range(len(S)):
    Sa[i + 1] += Sa[i]
    Sb[i + 1] += Sb[i]

for i in range(len(T)):
    if T[i] == "A":
        Ta[i + 1] = 1
    else:
        Tb[i + 1] = 1
for i in range(len(T)):
    Ta[i + 1] += Ta[i]
    Tb[i + 1] += Tb[i]

ok_group = {
    ((0, 1), (2, 0), (1, 2)),
    ((0, 2), (2, 1), (1, 0)),
    ((1, 1), (0, 0), (2, 2))
}

for i in range(q):
    a, b, c, d = list(map(int, readline().split()))
    s = ((Sa[b] - Sa[a - 1]) % 3, (Sb[b] - Sb[a - 1]) % 3)
    t = ((Ta[d] - Ta[c - 1]) % 3, (Tb[d] - Tb[c - 1]) % 3)
    if s == t:
        print("YES")
        continue
    for ok in ok_group:
        if s in ok and t in ok:
            print("YES")
            break
    else:
        print("NO")
