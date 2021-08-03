def count_pal(n): return [int('9' + '0' * (n // 2 - int(not n & 1))), int([['1', '10'][n & 1] + '9' * (n // 2 - 1) + '8', '9'][n == 1])]
