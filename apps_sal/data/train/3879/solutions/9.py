def search(budget,prices):
    return ",".join(str(price) for price in sorted(prices) if price <= budget)
