def cost_of_carpet(room_length, room_width, roll_width, roll_cost):
    if 0 in [room_length, room_width]:
        return 'error'
    (mi, mx) = (min((room_length, room_width)), max((room_length, room_width)))
    (rw, rc) = (roll_width, roll_cost)
    return round(mi * rw * rc, 2) if mx <= roll_width else round(mx * rw * rc, 2) if roll_width >= mi else 'error'
