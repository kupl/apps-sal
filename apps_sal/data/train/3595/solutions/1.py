from collections import Counter


def swap_them(a, b):
    cnt = Counter(b.lower())
    return ''.join((c.swapcase() if cnt[c.lower()] % 2 else c for c in a))


def work_on_strings(a, b):
    return swap_them(a, b) + swap_them(b, a)
