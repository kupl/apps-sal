from textwrap import wrap


def split_in_parts(s, part_length):
    return ' '.join(wrap(s, part_length))
