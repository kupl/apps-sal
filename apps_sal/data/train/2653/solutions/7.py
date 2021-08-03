def bingo(a):
    return "WIN" if all([x in a for x in [2, 7, 9, 14, 15]]) else "LOSE"
