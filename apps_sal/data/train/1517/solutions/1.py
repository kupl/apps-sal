import sys
T = int(sys.stdin.readline())
while T:
    (n, k) = list(map(int, input().split()))
    num = list(map(int, sys.stdin.readline().split()))
    den = list(map(int, sys.stdin.readline().split()))
    ans = n
    for i in range(k):
        ans += ans * num[i] / float(den[i])
    print(int(100 - 100 * n / ans))
    T -= 1
