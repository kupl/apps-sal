def michael_pays(c):
    return round(max(c if c < 5 else c * 2/3, c - 10), 2)
