def divisors(n):
    count = 0
    div_by_n = 0
    while count < n:
        count += 1
        if n % count == 0:
            div_by_n += 1
    return div_by_n
