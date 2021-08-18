mod = 10**9 + 7

for k in range(int(input())):
    num, times = map(int, input().split())

    if num == 0:
        x = times - 1
        ans = (((x % mod) * (x % mod)) % mod + x % mod) % mod
    else:
        if times % 2 == 0:
            x = num + (times - 1) // 2
            ans = ((((x % mod) * (x + 1) % mod) + x % mod) + num % mod - x % mod) % mod
        else:
            x = num + (times - 1) // 2
            ans = ((((x % mod) * (x + 1) % mod) + x % mod) - num % mod - x % mod) % mod

    print(ans)
