def product_way(n, start=2):
    result = 0
    for i in range(start, n//2+1):
        if n%i == 0 and i<=n/i:
            result += 1 + product_way(n//i, i)
    return result


def prod_int_part(n):
    x = product_way(n, 2)
    y = []
    m = n
    for i in range(2, n//2+1):
        if n%i == 0:
            while (m%i == 0):
                m /= i
                y.append(i)
    return [x, y]
