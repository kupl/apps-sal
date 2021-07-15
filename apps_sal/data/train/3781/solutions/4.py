from math import sqrt

def partitions(n, floor = 2):
    parts = [[n]]
    for i in range(floor, int(sqrt(n)) + 1):
        if n % i == 0:
            for part in partitions(n // i, i):
                parts.append([i] + part) 
    return parts

def prod_int_partII(n, s):
    lists = []
    parts = partitions(n, 2)
    for part in parts:
        if len(part) == s:
            lists.append(part)
    if len(lists) == 1:
        list = lists[0]
    else:
        list = lists
    return [len(parts) - 1, len(lists), list]
