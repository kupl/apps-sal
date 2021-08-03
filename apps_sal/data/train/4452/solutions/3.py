def maximum_product_of_parts(n: int) -> int:
    n = str(n)
    return max([int(n[:i]) * int(n[i:j]) * int(n[j:]) for i in range(1, len(n) + 1) for j in range(i + 1, len(n))])
