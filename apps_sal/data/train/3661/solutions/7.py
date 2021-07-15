def find_part_max_prod(n):
    if n % 3 == 0:
        Q = n//3
        return [[3]*Q, 3**Q]
    elif (n - 1) % 3== 0:
        Q = (n-1)//3 - 1
        return [[4]+[3]*Q,[3]*Q+[2,2], 4*3**Q]
    elif (n - 2) % 3 == 0:
        Q = (n-2)//3
        return [[3]*Q+[2], 2*3**Q]
