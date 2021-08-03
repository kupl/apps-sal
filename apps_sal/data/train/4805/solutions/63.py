def check(seq, element):
    """(^__^)"""
    flag = []
    for elem in seq:
        if elem == element:
            flag.append(1)
        else:
            flag.append(0)

    if sum(flag) > 0:
        return True
    else:
        return False
