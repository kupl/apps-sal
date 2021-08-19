def partitions(s):
    if s:
        for i in range(1, len(s) + 1):
            for p in partitions(s[i:]):
                yield ([s[:i]] + p)
    else:
        yield []


def add_values(product_string):
    product_list = partitions(product_string)
    return sum([sum(map(int, items)) for items in list(product_list)[:-1]])


def next_higher(start_value, k):
    product = (start_value + 1) * k
    while add_values(str(product)) != start_value:
        start_value += 1
        product = start_value * k
    return start_value
