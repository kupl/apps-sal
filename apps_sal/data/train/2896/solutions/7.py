from math import ceil


def cost_of_carpet(room_length, room_width, roll_width, roll_cost):
    (w, l) = sorted([room_length, room_width])
    if room_length == 0 or room_width == 0 or roll_width < w:
        return 'error'
    if l <= roll_width:
        return round(w * roll_width * roll_cost, 2)
    else:
        return round(l * roll_width * roll_cost, 2)
