def bin_insert(n, lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        check = (start + end) // 2
        if lst[check] == n:
            return check
        if lst[check] < n:
            start = check + 1
        else:
            end = check - 1
    if len(lst) != 0 and lst[start] < n:
        return start + 1
    return start


def comb(fruits):
    fruits.sort()
    res = 0
    while len(fruits) > 1:
        wt = fruits.pop(0) + fruits.pop(0)
        res += wt
        fruits.insert(bin_insert(wt, fruits), wt)
    return res
