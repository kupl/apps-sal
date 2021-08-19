def press_button(n):
    return sum((i * (n - i) for i in range(1, n))) + n
