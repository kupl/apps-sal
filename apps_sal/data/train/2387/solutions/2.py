t = int(input())
for i in range(t):
    n = int(input())
    res = 0
    while n > 9:
        res += n // 10 * 10
        n = n // 10 + n % 10
    res += n
    print(res)

