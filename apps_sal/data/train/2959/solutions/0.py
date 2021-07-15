from functools import lru_cache


def optimal_number_of_coins(n, coins):
    @lru_cache(maxsize=None)
    def f(amount: int, idx: int) -> float:
        q, r = divmod(amount, coins[idx])
        if r == 0:
            return q
        elif amount < 0 or idx <= 0:
            return float("inf")
        else:
            return min(1 + f(amount - coins[idx], idx), f(amount, idx - 1))

    coins = sorted(set(coins))
    return f(n, len(coins) - 1)
