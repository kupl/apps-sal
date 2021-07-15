def squares_needed(grains):
    cnt = 0
    n = 1
    while n <= grains:
        n = n * 2
        cnt = cnt + 1
    return cnt
