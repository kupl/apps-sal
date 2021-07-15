def womens_age(n):
    base = (n//2)
    if n % 2 == 0:
        return f"{n}? That's just 20, in base {base}!"
    else:
        return f"{n}? That's just 21, in base {base}!"
