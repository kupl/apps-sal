
max_ = int(2e5)


def make_arr(dp):
    dp[1] = 2
    for i in range(2, max_):
        dp[i] = dp[i - 1] + i


dp = [0] * (max_ + 1)
make_arr(dp)
M, N = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
A.sort(reverse=True)
ans = 0
flag = 0
for i in A:
    if(flag == 0):
        if(N >= i):
            ans = ans + dp[i]
            N = N - i
        elif(N < i):
            ans = ans + dp[N]
            flag = 1
    else:
        ans = ans + 1

print(ans)
