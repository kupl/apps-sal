def distribution_of(golds):
    golds_list = golds[:]
    a = []
    b = []
    turn = 1
    while len(golds_list) > 0:
        if golds_list[0] >= golds_list[-1]:
            value = golds_list.pop(0)
        else:
            value = golds_list.pop(-1)
        if turn % 2 == 1:
            a.append(value)
        else:
            b.append(value)
        turn += 1
    return [sum(a), sum(b)]
