def sum_mul(n, m):
    if m < 1 or n < 1:
        return "INVALID"
    else:
        grandtotal = []
        subtotal = 0
        for i in range(1, m):
            if i % n == 0:
                subtotal = subtotal + i
                grandtotal.append(i)
        return sum(grandtotal)
