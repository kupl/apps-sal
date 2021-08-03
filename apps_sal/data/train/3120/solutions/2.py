def meeting(rooms, n):
    if n == 0:
        return "Game On"
    chairs, res = (max(0, chair - len(occ)) for occ, chair in rooms), []
    for c in chairs:
        if c >= n:
            return res + [n]
        res.append(c)
        n -= c
    return "Not enough!"
