def distribution_of(golds):
    gold_list = golds[:]
    isA = True
    amount = [0, 0]
    while len(gold_list) != 0:
        if gold_list[0] > gold_list[-1] or gold_list[0] == gold_list[-1]:
            if isA:
                amount[0] += gold_list[0]
            else:
                amount[1] += gold_list[0]
            gold_list.pop(0)
        else:
            if isA:
                amount[0] += gold_list[-1]
            else:
                amount[1] += gold_list[-1]
            gold_list.pop(-1)
        isA = not isA
    return amount
