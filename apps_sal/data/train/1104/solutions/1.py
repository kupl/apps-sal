t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    M = 1000000007
    if(n == 0):
        m = k - 1
        total = (m * (m + 1))
        print(total % M)
    else:
        if(k % 2 == 0):
            m = (k - 2) // 2 + n
            total = (m * (m + 1)) + n
            print(total % M)
        else:
            m = (k) // 2 + n
            total = (m * (m + 1)) - n
            print(total % M)
