from bisect import bisect_left
from collections import deque


def find_discounted(prices: str) -> str:
    all_prices = deque(list(map(int, prices.split())))
    discounts = []
    while all_prices:
        d = all_prices.popleft()
        discounts.append(d)
        del all_prices[bisect_left(all_prices, d * 4 // 3)]
    return ' '.join(map(str, discounts))
