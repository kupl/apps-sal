def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(sum(parity) == 1)]
