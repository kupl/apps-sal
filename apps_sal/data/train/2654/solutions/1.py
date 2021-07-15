def michael_pays(c):
    return round(c if c < 5 else c * 2 / 3 if c <= 30 else c - 10, 2)
