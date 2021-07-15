def same_col_seq(val, k, col):
    colDct = {'red': 1, 'blue': 0}

    def gen():
        n = ((1 + 24*val/3)**.5 - 1)//2
        while True:
            n += 1
            s = n*(n+1)/2
            if s%3 == colDct[col]: yield s
            
    g = gen()
    return [next(g) for _ in range(k)] if col != 'yellow' else []
