def list_squared(m, n):
    res = []
    for num in range(m, n):
        div_sum = sum(i * i + ((num // i) * (num // i) if num // i != i else 0) for i in range(1, int(num**0.5) + 1) if num % i == 0)
        root = div_sum ** 0.5
        if root.is_integer():
            res.append([num, div_sum])
    return res
