def max_number(n):
    r = list(str(n))
    k = sorted(r, reverse = True)
    p = ",".join(k)
    return int(p.replace(",",""))

