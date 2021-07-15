def sale_hotdogs(n):
    return {0: 100, 1: 95}.get(n // 5, 90) * n
