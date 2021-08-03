def update_score(current_score, called_trump, alone, tricks):
    a = current_score[:]
    w = tricks.count(called_trump)
    if w < 3:
        a[(called_trump - 1) ^ 1] += 2
    else:
        a[called_trump - 1] += 1 if w < 5 else 4 if alone else 2
    return a
