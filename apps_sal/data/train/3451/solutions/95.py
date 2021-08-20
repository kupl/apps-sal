import functools
import itertools


def triangle(row):

    def next_level(level_row):
        if len(level_row) > 2:
            return ''.join([next_level(level_row[i:i + 2]) for i in range(len(level_row)) if len(level_row[i:i + 2]) > 1])
        str_list = ''.join(sorted([level_row[0], level_row[1]]))
        if level_row[0] == level_row[1]:
            return level_row[0]
        return {'GR': 'B', 'BG': 'R', 'BR': 'G'}.get(str_list)
    result = row
    while len(result) > 1:
        result = next_level(result)
    return result
