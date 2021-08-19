import math


def complete_binary_tree(a):
    ret = []
    rows = [a]

    while len(rows):
        newrows = []
        # print(rows)
        for x in rows:
            ln = len(x)
            if ln > 1:
                pwr = int(math.log(ln + 1, 2))
                complete_part_ln = 2**pwr - 1
                last_full_row_ln = 2**(pwr - 1)
                free_row_ln = ln - complete_part_ln
                middle = complete_part_ln // 2 + (last_full_row_ln if free_row_ln > last_full_row_ln else free_row_ln)
                ret += [x[middle]]
                newrows += [x[:middle]] + [x[middle + 1:]]
            else:
                ret += x
        rows = newrows

    return ret
