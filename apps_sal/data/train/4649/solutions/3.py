from itertools import takewhile, accumulate


def get_section_id(scroll, sizes):
    return -1 if sum(sizes) <= scroll else sum(1 for _ in takewhile(scroll.__ge__, accumulate(sizes)))
