def withdraw(n, coins=(100, 50, 20)):
    if not n:
        return [0] * len(coins)
    for i in range(n // coins[0] if coins else -1, -1, -1):
        sub = withdraw(n - i * coins[0], coins[1:])
        if sub is not None:
            return [i] + sub
