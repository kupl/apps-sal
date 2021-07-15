def order_weight(string):
    return str(' '.join(sorted(sorted(string.split()), key = lambda x:sum(map(int, str(x))))))
