POINTS = [[0, 2],    # 0 tricks ; index 0 = caller ; 1 = opponent
          [0, 2],    # 1 tricks
          [0, 2],    # 2 tricks
          [1, 0],    # 3 tricks
          [1, 0],    # 4 tricks
          [2, 0], ]   # 5 tricks


def update_score(current_score, called_trump, alone, tricks):
    n_tricks = tricks.count(called_trump)
    inc = POINTS[n_tricks][:]
    if called_trump == 2:
        inc.reverse()
    return [v + inc[i] + 2 * (i == called_trump - 1 and n_tricks == 5 and alone) for i, v in enumerate(current_score)]
