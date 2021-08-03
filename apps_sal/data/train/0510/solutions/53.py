import bisect

N = int(input())
S = list(str(input()))


def ci(x):
    return "abcdefghijklmnopqrstuvwxyz".find(x)


d = [[] for _ in range(26)]
for i, s in enumerate(S):
    d[ci(s)].append(i)

for i in range(int(input())):
    t, x, y = input().split()
    if t == "1":
        x = int(x) - 1
        if S[x] != y:
            l = bisect.bisect_left(d[ci(S[x])], x)
            d[ci(S[x])].pop(l)
            bisect.insort(d[ci(y)], x)
            S[x] = y
    else:
        x, y = int(x) - 1, int(y) - 1
        c = 0
        for j in range(26):
            l = bisect.bisect_left(d[j], x)
            if l < len(d[j]) and d[j][l] <= y:
                c += 1
        print(c)
