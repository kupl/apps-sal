def penaltyShots(shots, score):
    a, b = score
    return 6 - shots - abs(a-b) if shots < 5 else 2 - (a != b)
