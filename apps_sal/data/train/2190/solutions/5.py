n = int(input())
A = list(map(int, input().strip().split()))[::-1]
p = 0
p_max = 0
X = []
for i in A:
    while(len(X) > 0 and X[-1][0] < i):
        p = max((p + 1, X[-1][1]))
        X.pop()
    X.append((i, p))
    if p > p_max:
        p_max = p
    p = 0
print(p_max)
