def pac_man(n, pm, enemies):
    left, right, top, floor = -1, n, -1, n
    for y, x in enemies:
        if top < y < pm[0]: 
            top = y
        if pm[0] < y < floor: 
            floor = y
        if left < x < pm[1]: 
            left = x
        if pm[1] < x < right: 
            right = x
    return (right - left -1) * (floor - top - 1) - 1

