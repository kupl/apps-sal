from math import gcd
def min_price(coins):
    if 1 in coins:
        return 1

# Round Robin Algorithm [from https://pdfs.semanticscholar.org/14ac/14a15ebc31b58a4ac04328f9824f743a1e4e.pdf]
    coins = sorted(coins)
    myinf = 4000000000
    n = [0] + [myinf] * (coins[0] - 1)
    for i in range(1, len(coins)):
        d = gcd(coins[0], coins[i])
        for r in range(0, d):
            nn = min([n[q] for q in range(r, r + coins[0] - d + 1, d)])
            if nn != myinf:
                for j in range(0, coins[0] // d):
                    nn = nn + coins[i]
                    p = nn % coins[0]
                    nn = min(nn, n[p])
                    n[p] = nn

    maxn = max(n)
    if maxn == myinf:
        return -1

    return max(n) - coins[0] + 1

