def mult_triangle(n):
    (even, sum, i) = (0, 0, 1)
    while i <= n:
        sum += i * i * i
        even += i * (i - 1) * (i + 1) / 2 if i % 2 else i * i * i
        i += 1
    return [sum, even, sum - even]
