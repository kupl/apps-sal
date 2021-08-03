def crossing_sum(mx, r, c):
    return sum(mx[r] + [x[c] for x in mx[:r] + mx[r + 1:]])
