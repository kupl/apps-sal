def sale_hotdogs(n):
    total = 0
    for i in range(n):
        if n < 5:
            total += 100

        elif 5 <= n < 10:
            total += 95

        else:
            total += 90

    return total
