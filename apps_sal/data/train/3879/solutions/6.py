def search(budget,prices):
    return ','.join(str(num) for num in sorted(prices) if num <= budget)
