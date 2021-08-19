from collections import defaultdict


def group_in_10s(*nums):
    dct = defaultdict(list)
    for n in sorted(nums):
        dct[n // 10].append(n)
    return [dct.get(i) for i in range(max(dct) + 1)] if nums else []


# alternative without import
# def group_in_10s(*nums):
#    s = sorted(nums)
#    lst = [[] for _ in range(s[-1] // 10 + 1)] if nums else []
#    for n in s:
#        lst[n//10].append(n)
#    return [l or None for l in lst]
