def cost_of_carpet(l, w, roll, cost):
    if l > roll < w or l <= 0 or w <= 0:
        return 'error'
    res = 0
    if l <= roll < w:
        res = roll * w * cost
    elif w <= roll < l:
        res = roll * l * cost
    else:
        res = roll * min(w, l) * cost
    return round(res, 2)
