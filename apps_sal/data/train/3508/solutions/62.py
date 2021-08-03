def halving_sum(n):
    a = []
    for i in range(n):
        a.append(n)
        n = int(n / 2)
        if int(n) >= 1:
            pass
        else:
            break
    return sum(a)
