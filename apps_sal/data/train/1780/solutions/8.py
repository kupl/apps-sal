from operator import mul
from functools import reduce


mem = {}


def cache(func):
    def wrap(n):
        if n in mem:
            return mem[n]
        res = func(n)
        mem[n] = res
        return res
    return wrap


@cache
def int_partition(n):
    if n in mem:
        return mem[n]
    if n == 1:
        return {(1,)}
    part_set = int_partition(n - 1)
    result = set()
    for part in list(part_set):
        num_set = set(part)
        for num in num_set:
            tmp = list(part)
            i = part.index(num)
            tmp[i] += 1
            result.add(tuple(tmp))
        result.add(part + tuple([1]))
    return result


def part(n):
    res = {}
    part_set = int_partition(n)
    prod_set = set()
    for part_one in part_set:
        prod_set.add(reduce(mul, part_one, 1))
    prod_list = sorted(list(prod_set))

    res['range'] = prod_list[-1] - prod_list[0]
    res['avg'] = float(sum(prod_list)) / len(prod_list)
    mid = int((float(len(prod_list) - 1) / 2))
    rev_mid = -mid if mid else None
    mid_slice = prod_list[mid:rev_mid]
    res['median'] = float(sum(mid_slice)) / len(mid_slice)

    tmpl = 'Range: {range} Average: {avg:.2f} Median: {median:.2f}'
    return tmpl.format(**res)
