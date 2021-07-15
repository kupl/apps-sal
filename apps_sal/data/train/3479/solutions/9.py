def part_const(n, k, num, s=0, startwith=1):
    if k == 1:
        if n - s >= startwith and n - s != num:
            return 1
        return 0
    result = 0
    for i in range(startwith, n - s - k + 2):
        if i == num:
            continue
        result += part_const(n, k-1, num, s + i, i)
    return result
    

