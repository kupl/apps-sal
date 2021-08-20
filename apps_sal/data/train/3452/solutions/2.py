def snail(height, day, night):
    (n, r) = divmod(max(0, height - day), day - night)
    return n + 1 + (r != 0)
