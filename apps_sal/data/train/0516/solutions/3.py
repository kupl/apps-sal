# cook your dish here
def sree(k, n, m):
    sum1 = (m * (m + 1)) // 2
    sum2 = (m * (m - 1)) // 2
    shanth = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if i < j and k[i] > k[j]:
                shanth += sum1
            elif j < i and k[i] > k[j]:
                shanth += sum2
    return shanth


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    k = list(map(int, input().split()))
    print(sree(k, n, m))
