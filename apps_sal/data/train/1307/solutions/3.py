e = 10**9 + 7
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    messi = 0
    non_messi = k
    for i in range(n - 2):
        z = non_messi
        non_messi = (messi * k + z * (k - 1)) % e
        messi = z

    print(non_messi)
