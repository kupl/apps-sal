POINTS = [[0, 2],
          [0, 2],
          [0, 2],
          [1, 0],
          [1, 0],
          [2, 0], ]


def update_score(current_score, called_trump, alone, tricks):
    n_tricks = tricks.count(called_trump)
    inc = POINTS[n_tricks][:]
    if called_trump == 2:
        inc.reverse()
    return [v + inc[i] + 2 * (i == called_trump - 1 and n_tricks == 5 and alone) for i, v in enumerate(current_score)]
