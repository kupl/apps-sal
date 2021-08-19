def adjacent_element_product(p):
    return max((p[i] * p[-~i] for i in range(~-len(p))))
