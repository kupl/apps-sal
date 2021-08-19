def starting_mark(height):
    # your code here
    # 9.45-1.52 =7.93    10.67-1.83= 8.84
    # 9.45 = m(1.52) + b // 10.67 = m(1.83) + b
    # 1.22 = 0.31m  ==> 3.94 = m and b = 3.46
    m = 1.22 / 0.31
    b = 10.67 - (1.83 * m)
    return float("{:.2f}".format(round(m * height + b, 2)))
