def maximum_product_of_parts(n):
    return (lambda s: max((int(s[:i]) * int(s[i:j]) * int(s[j:]) for j in range(2, len(s)) for i in range(1, j))))(str(n))
