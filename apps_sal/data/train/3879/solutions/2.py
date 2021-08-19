def search(budget, prices):
    return ','.join(map(str, sorted([n for n in prices if n <= budget])))
