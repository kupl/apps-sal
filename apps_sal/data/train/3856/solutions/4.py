def list_simple_num(a):
    lst = list(range(a + 1))
    lst[1] = 0
    for l in lst:
        if l != 0:
            for j in range(2 * l, len(lst), l):
                lst[j] = 0
    return lst


def solve(a, b):
    lst = tuple(filter(bool, list_simple_num(b)))
    ind = list_simple_num(len(lst))[1:]
    return sum((lst for (ind, lst) in zip(ind, lst) if ind != 0 and lst > a))
