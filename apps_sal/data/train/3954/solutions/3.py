def press_button(n):
    return n + sum((i * (n - i) for i in range(1, n)))
