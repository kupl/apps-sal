def solve(lis, n):
    cnt = 0
    for i in range(1, n):
        val = lis[i] & lis[i - 1]
        if val != lis[i - 1]:
            return -1
        cnt += bin(val).count('1')
    return 2 ** cnt % mod


for t in range(int(input())):
    n = int(input())
    lis = list(map(int, input().split()))
    mod = int(1000000000.0) + 7
    ans = solve(lis, n)
    print(0 if ans == -1 else ans)
