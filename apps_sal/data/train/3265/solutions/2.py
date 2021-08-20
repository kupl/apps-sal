def get_totals_for_row(n):
    total = n ** 3
    if n % 2 == 0:
        return [total, total, 0]
    else:
        even_total = n * (n ** 2 // 2)
        odd_total = total - even_total
        return [total, even_total, odd_total]


def mult_triangle(n):
    total = 0
    even_total = 0
    odd_total = 0
    for level in range(1, n + 1):
        (t, e, o) = get_totals_for_row(level)
        total += t
        even_total += e
        odd_total += o
    return [total, even_total, odd_total]
