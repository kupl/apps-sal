def minutes(s):
    return int(s[0:2]) * 60 + int(s[-2:])


def timeformat(m):
    return "{:02d}:{:02d}".format(m // 60, m % 60)


def solve(arr):
    arr = list(set(arr))
    m = [minutes(arr) for arr in sorted(arr)]
    difference = [(m[(i + 1) % len(m)] - a - 1) % (60 * 24) for i, a in enumerate(m)]

    return(timeformat(max(difference)))
