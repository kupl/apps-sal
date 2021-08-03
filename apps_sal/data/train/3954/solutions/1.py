def press_button(n):
    return sum((n - i) * (i + 1) - i for i in range(n))
