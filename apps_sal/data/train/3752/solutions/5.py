def value_at(poly_spec, x):
    leng = len(poly_spec)
    ans = 0
    for i, e in enumerate(poly_spec):
        temp = 1
        for j in range(leng-i-1):
            temp *= (x-j)/(j+1)
        ans += e*temp
    return round(ans, 2)
