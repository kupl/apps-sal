def num_primorial(n):
    p = []
    val = 2
    while len(p) < n:
        for div in p:
            if val % div == 0:
                val += 1
                break
        else:
            p.append(val)
    val = 1
    for x in p:
        val *= x
    return val
