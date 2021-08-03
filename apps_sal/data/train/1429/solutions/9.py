for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(float, input().split()))
    ans = 0
    for i in range(30):
        temp = 0
        for j in range(n):
            if (a[j] & (1 << i)):
                temp = temp * (1 - b[j]) + (1 - temp) * b[j]
        ans += temp * (1 << i)
    print(ans)
