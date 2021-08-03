def count(lst, target, mod):
    if mod == 0:
        return lst.count(target)
    return sum((n - target) % mod == 0 for n in lst)
