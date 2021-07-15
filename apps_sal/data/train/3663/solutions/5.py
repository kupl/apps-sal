def four_piles(n,y):
    candidates = ([x+y, x-y, x*y, x/y] for x in range(y+1, int(n)-y+1))
    return next((candidate for candidate in candidates if sum(candidate) == n), [])
