def row_sum_odd_numbers(n):
    count = 0
    kokosik = 1
    result = 0
    for huesosina in range(0, n):
        kokosik += count
        count += 2
    result += kokosik
    for guccigang in range(0, n - 1):
        kokosik += 2
        result += kokosik
    return result
