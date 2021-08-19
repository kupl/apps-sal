import sys
from functools import partial
SAMPLE_IN = 'sample.in'
SAMPLE_ANS = 'sample.ans'


def read_int(f) -> int:
    return int(f.readline())


def read_ints(f) -> list:
    return [int(x) for x in f.readline().split()]


def read_case(f=sys.stdin) -> tuple:
    n = read_int(f)
    nums = read_ints(f)
    return (n, nums)


def solve(n, nums):
    even = 0
    odd = [-1] * (n + 1)
    for x in nums:
        (even, odd[x]) = (max(even, odd[x] + 1), even + 1)
    return n - even


def make_submission(fin=sys.stdin, fout=sys.stdout):
    output = partial(print, file=fout)
    n_cases = int(fin.readline())
    for t in range(1, n_cases + 1):
        case = read_case(fin)
        answer = solve(*case)
        output(answer)


def __starting_point():
    import os
    if os.getenv('GCJ_LOCAL'):
        with open(SAMPLE_IN) as s:
            make_submission(s)
    else:
        make_submission()


__starting_point()
