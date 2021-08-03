def bingo(array):
    return "WIN" if all(i in array for i in [2, 9, 14, 7, 15]) else "LOSE"
