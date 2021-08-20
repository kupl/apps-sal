ans = 0
t = int(input())
i = 1
while i <= t:
    n = int(input())
    ans = 0
    while n > 0:
        ans += n % 10
        n = int(n / 10)
        if n > 0:
            continue
    i = i + 1
    print(ans)
