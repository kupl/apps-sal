def sale_hotdogs(n):
    if n >= 10:        return 90 * n
    elif 5 <= n < 10:  return 95 * n
    elif 5 > n:        return 100 * n
    else:              return 0
