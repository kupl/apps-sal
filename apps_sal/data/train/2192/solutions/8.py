dp = []


def fun(n, a):
    dp[0] = 1
    for i in range(1, n):
        l, r = 0, i - 1
        while l <= r:
            m = (l + r) >> 1
            if a[i][0] - a[m][0] <= a[i][1]:
                r = m - 1
            else:
                l = m + 1
        #print (i, x)
        dp[i] = dp[r] + 1


n = int(input())
dp = [0 for i in range(n)]
a = []
for i in range(n):
    l = list(map(int, input().split()))
    a.append(l)
a.sort()
power = [0 for i in range(n)]

fun(n, a)
#print (dp)
print(n - max(dp))
