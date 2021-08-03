# cook your dish here
T = int(input())

for _ in range(T):
    N = int(input())
    ans = (N * N * N)
    for i in range(1, N):
        v = 2 * i * i * i
        ans = ans + v

    print(ans)
