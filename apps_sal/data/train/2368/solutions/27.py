from sys import stdin, stdout


T = int(stdin.readline())
for _ in range(T):

    N = int(stdin.readline())

    a = [int(x) for x in stdin.readline().split()]
    b = [int(x) for x in stdin.readline().split()]

    amn = min(a)
    bmn = min(b)

    ans = 0
    for i in range(N):
        ans += max(a[i] - amn, b[i] - bmn)
    print(ans)
