def update_score(current_score, called_trump, alone, tricks):
    w = tricks.count(called_trump)
    current_score[(w > 2) - called_trump] += 2 - (2 < w < 5) + 2 * (w == 5) * alone
    return current_score
