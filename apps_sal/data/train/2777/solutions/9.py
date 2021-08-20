from re import sub


def solve(st):
    while True:
        (st, tmp) = (sub('(\\d)*\\((\\w+)\\)', lambda s: s.group(2) * int(s.group(1) or 1), st), st)
        if st == tmp:
            return st
