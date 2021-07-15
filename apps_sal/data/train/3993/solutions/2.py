def solve(a):
    diff = 0
    for e in a:
        if type(e) == int:
            if e % 2:
                diff -= 1
            else:
                diff += 1
    return diff
