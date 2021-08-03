for _ in range(int(input())):
    s, n = list(map(int, input().split()))
    coins = 0
    if s <= n or s == 1:
        coins = (1) if (s % 2 == 0 or s == 1) else (2)
        print(coins)
    else:
        while n > 0:
            if n > s:
                n = s if s % 2 == 0 else s - 1
            else:
                coins += s // n
                s = s % n
                n = n - 2
        print(coins + s)
