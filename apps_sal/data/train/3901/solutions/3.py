def check_digit(n, i, j, x):
    i, j = sorted([i, j])
    return str(x) in str(n)[i:j + 1]
