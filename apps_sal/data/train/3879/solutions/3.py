def search(budget, prices):
    return ','.join(map(str, sorted(filter(float(budget).__ge__, prices))))
