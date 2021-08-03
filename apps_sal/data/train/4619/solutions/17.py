def whoseMove(b, w): return 'bwlhaictke'[(b < 'w') + w & 1::2]
