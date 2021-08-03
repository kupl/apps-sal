def target_game(values):
    sum1 = 0
    sum2 = 0
    for value in values:
        sum1 = max(sum1 + value, sum2)
        sum1, sum2 = sum2, sum1
    return max(sum1, sum2)
