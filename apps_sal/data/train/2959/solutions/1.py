def optimal_number_of_coins(n, coins):
    s = [0] * (n + 1)
    for c in coins:
        if c <= n:
            s[c] = 1
    for i in range(n + 1):
        s[i] = min((s[i - v] + 1 for v in coins if i - v >= 0), default=0)
    return s[n]
