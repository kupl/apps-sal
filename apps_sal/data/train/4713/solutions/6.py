from itertools import permutations

def late_clock(digits):
    mx = max(t for t in [''.join(p) for p in permutations(''.join(str(d) for d in digits))] if t[:2] < '24' and t[2:] < '60')
    return '{}:{}'.format(mx[:2], mx[2:])
