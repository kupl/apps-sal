def sale_hotdogs(n):
    return (100, 95, 90)[sum((n > 4, n > 9))] * n
