def feast(beast, dish):
    bf, bl = beast[0], beast[-1]
    df, dl = dish[0], dish[-1]
    return (bf, bl) == (df, dl)
