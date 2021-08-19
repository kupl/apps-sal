def cheapest_quote(n):
    s1 = n // 40
    y1 = n % 40
    s2 = y1 // 20
    y2 = y1 % 20
    s3 = y2 // 10
    y3 = y2 % 10
    s4 = y3 // 5
    y4 = y3 % 5
    return float('%.2f' % (s1 * 3.85 + s2 * 1.93 + s3 * 0.97 + s4 * 0.49 + y4 * 0.1))
