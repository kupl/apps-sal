def list_squared(m, n):
    result = []
    for i in range(m, n + 1):
        divisor = {1, i}
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                divisor.add(j)
                divisor.add(int(i / j))
        div_sq_sum = sum([k ** 2 for k in divisor])
        if div_sq_sum ** 0.5 == int(div_sq_sum ** 0.5):
            result.append([i, div_sq_sum])
    return result
