from itertools import chain

def split_by_value(k, arr):
    lst = [[],[]]
    for v in arr: lst[v>=k].append(v)
    return list(chain(*lst))
