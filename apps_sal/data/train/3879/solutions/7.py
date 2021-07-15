def search(budget,prices):
    prices.sort()
    return ','.join(str(x) for x in prices if x<=budget)
