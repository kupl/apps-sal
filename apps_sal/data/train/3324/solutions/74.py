def sale_hotdogs(n):
    price = {
        n < 5: n * 100,
        5 <= n < 10: n * 95,
        n >= 10: n * 90
    }
    return price.get(True)
