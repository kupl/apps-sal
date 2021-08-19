def search(budget, prices):
    return ','.join(map(str, sorted([x for x in prices if x <= budget])))
