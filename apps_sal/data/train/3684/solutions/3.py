def is_orthogonal(u, v):
    dot_product = 0
    for pair in zip(u, v):
        dot_product += pair[0] * pair[1]
    return dot_product == 0
