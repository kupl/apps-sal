from itertools import accumulate


def get_section_id(scroll, sizes):
    return next((i for (i, x) in enumerate(accumulate(sizes)) if x > scroll), -1)
