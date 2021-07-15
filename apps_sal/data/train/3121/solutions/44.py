def solve(a):
    for n in a:
        if -n in a:
            continue
        else:
            return n
