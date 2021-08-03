def find_discounted(prices):
    prices = [int(n) for n in prices.split()]
    return " ".join(prices.remove(round(p * 4 / 3)) or str(p) for p in prices)
