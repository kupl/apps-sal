N = int(input())
A = list(map(int, input().split()))
ans = [0] * N
numList = [(a, i) for (i, a) in enumerate(A)]
numList.sort(reverse=True)
numList.append((0, 0))
y = float('inf')
for (c, (a, i)) in enumerate(numList[:N], start=1):
    y = min(y, i)
    ans[y] += c * (a - numList[c][0])
print(*ans, sep='\n')
