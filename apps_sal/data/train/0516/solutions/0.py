def count(k, n, m):
    sum1 = (m * (m + 1)) // 2
    sum2 = (m * (m - 1)) // 2
    ct = 0
    for i in range(n):
        for j in range(n):
            if i < j and k[i] > k[j]:
                ct += sum1
            elif j < i and k[i] > k[j]:
                ct += sum2
    return ct


test = int(input())
for _ in range(test):
    n, m = map(int, input().split())
    k = list(map(int, input().split()))
    print(count(k, n, m))
