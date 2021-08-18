def christmas_tree(h):
    return "" if h < 3 else "\r\n".join(["\r\n".join([" " * (((5 - y) // 2) + (h // 3) - i - 1) + "*" * (y + i * 2) for y in [1, 3, 5]]) for i in range(h // 3)]) + "\r\n" + " " * (h // 3) + "
