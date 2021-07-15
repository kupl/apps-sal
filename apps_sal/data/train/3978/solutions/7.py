def check_for_factor(base, factor):
    ans = False
    for x in range(base+1):
        if factor * x == base:
            ans = True
    return ans
