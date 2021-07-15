def update_score(current_score, called_trump, alone, tricks):
    n = tricks.count(called_trump)
    if n <= 2:
        called_trump = 3 - called_trump
        p = 2
    elif n <= 4:
        p = 1
    else:
        p = 4 if alone else 2
    current_score[called_trump > 1] += p
    return current_score
