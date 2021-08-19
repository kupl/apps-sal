def black_or_white_key(n):
    return 'bwlhaictke'[13 >> ~-n % 88 % 12 % 5 & 1::2]
