def womens_age(n):
    for i in range(11, 100):
        (a, b) = divmod(n, i)
        if a == 2 and b < 2:
            return f"{n}? That's just {a}{b}, in base {i}!"
