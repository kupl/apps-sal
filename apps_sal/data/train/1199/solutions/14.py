t = int(input())
for _ in range(t):
    s, n = map(int, input().split())
    if s < n:
        if s == 1:
            coins = 1
        elif s % 2 == 0:
            coins = 1
        else:
            coins = 2
    else:
        coins = s // n
        r = s % n
        if r == 1:
            coins = coins + 1
        elif r != 0 and r % 2 == 0:
            coins = coins + 1
        elif r % 2 != 0:
            coins = coins + 2
    print(coins)
