def gcd(a, b):
    while a:
        (b, a) = (a, b % a)
    return b


def min_price(coins):
    if 1 in coins:
        return 1
    coins.sort()
    print(coins)
    n = [0] + [-1] * (coins[0] - 1)
    for i in range(1, len(coins)):
        d = gcd(coins[0], coins[i])
        for r in range(d):
            try:
                nn = min((n[q] for q in range(r, coins[0], d) if n[q] != -1))
            except:
                continue
            if nn != -1:
                for c in range(coins[0] // d):
                    nn += coins[i]
                    p = nn % coins[0]
                    nn = min(nn, n[p]) if n[p] != -1 else nn
                    n[p] = nn
    if len(coins) < 2 or -1 in n:
        return -1
    return max(n) - coins[0] + 1
