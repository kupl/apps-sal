BINGO = {ord(c) - 64 for c in 'BINGO'}


def bingo(lst):
    return 'WIN' if set(lst) >= BINGO else 'LOSE'
