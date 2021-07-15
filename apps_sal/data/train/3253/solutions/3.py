def womens_age(n):
    return f"{n}? That's just {21 if n % 2 else 20}, in base {(n - 1) // 2 if n % 2 else n // 2}!"
