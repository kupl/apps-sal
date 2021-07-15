from bisect import bisect
from itertools import accumulate

def get_section_id(scroll, sizes):
    return bisect(list(accumulate(sizes)), scroll) if scroll < sum(sizes) else -1
