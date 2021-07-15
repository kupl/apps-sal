def draw_spider(leg_size, body_size, mouth, eye):
    if leg_size == 1:
        leg1 = '^'
        leg2 = '^'
    elif leg_size == 2:
        leg1 = '/\\'
        leg2 = '/\\'
    elif leg_size == 3:
        leg1 = "/╲"
        leg2 = "╱\\"
    else:
        leg1 = '╱╲'
        leg2 = '╱╲'
    return leg1 + body_size * '(' + \
           int(2**body_size/2) * eye + mouth + int(2**body_size/2) * eye + \
           body_size * ')' + leg2
