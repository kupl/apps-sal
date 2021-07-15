def pass_the_bill(total, cons, refs):
    inds = total - cons - refs
    boundary = total // 2 + 1
    if cons + inds < boundary:
        return -1
    if cons > boundary:
        return 0
    return boundary - cons
