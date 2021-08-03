from itertools import product


def proc_seq(*args):
    nums = set(int(''.join(l)) for l in product(*(str(a) for a in args)) if l[0] != '0')
    if len(nums) == 1:
        return [1, nums.pop()]
    return [len(nums), min(nums), max(nums), sum(nums)]
