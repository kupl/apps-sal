import sys
N = 80
ans = [1]
i = 1
while i < N:
    ans.append(ans[i - 1] * (2 * i - 1))
    i = i + 1
T = int(sys.stdin.readline().strip())
while T > 0:
    n = int(sys.stdin.readline().strip())
    print(ans[n])
    T = T - 1
