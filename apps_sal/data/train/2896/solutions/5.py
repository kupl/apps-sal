def cost_of_carpet(l, w, r, c):
    if l == 0 or w == 0 or (l > r and w > r):
        return 'error'
    return round((min(l, w) if l <= r and w <= r else max(l, w)) * r * c, 2)
