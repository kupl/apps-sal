T = int(input())
while T:
    N = int(input())
    A = list(map(int, input().split()))
    d = set()
    n = (N * (N + 1)) // 2
    if N > 60:
        print("NO")
    else:
        for i in range(N):
            ans = 0
            for j in range(i, N):
                ans = A[j] | ans
                d.add(ans)
        if len(d) == n:
            print("YES")
        else:
            print("NO")

    T -= 1
