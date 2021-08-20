def find_a(array, n):
    if n in [0, 1, 2, 3]:
        return array[n]
    b1 = 3 * array[1] - array[0] - array[2]
    b2 = 3 * array[2] - array[1] - array[3]
    if n > 3:
        ak = array[3]
        bk = 3 * b2 - b1 - array[2]
        ap = array[2]
        bp = b2
        i = 3
        while i < n:
            (ak, ap) = (3 * ak - bk - ap, ak)
            (bk, bp) = (3 * bk - ap - bp, bk)
            i += 1
        return ak
    else:
        ak = array[0]
        bk = 3 * b1 - b2 - array[1]
        ap = array[1]
        bp = b1
        i = 0
        while i > n:
            (ak, ap) = (3 * ak - bk - ap, ak)
            (bk, bp) = (3 * bk - ap - bp, bk)
            i -= 1
        return ak
