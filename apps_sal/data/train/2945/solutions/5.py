def fortune(f0, p, c0, n, i):
    year_checker = 0
    fn = f0
    cn = c0

    while(year_checker < n - 1):
        fn = int(fn + fn * (0.01 * p) - cn)
        cn = int(cn + cn * (0.01 * i))

        year_checker = year_checker + 1

    if(fn < 0):
        return False

    return True
