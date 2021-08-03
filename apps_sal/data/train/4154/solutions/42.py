def is_triangle(a, b, c):
    lts = [a, b, c]
    lts.sort()
    return(lts[2] < lts[1] + lts[0])
