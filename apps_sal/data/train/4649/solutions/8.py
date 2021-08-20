from itertools import accumulate


def get_section_id(scroll, sizes):
    return next((i for (i, s) in enumerate(accumulate(sizes)) if s > scroll), -1)
