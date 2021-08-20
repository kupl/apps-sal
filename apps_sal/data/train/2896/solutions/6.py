def cost_of_carpet(room_length, room_width, roll_width, roll_cost):
    if room_length <= 0 or room_width <= 0 or room_length > roll_width < room_width:
        return 'error'
    (x, y) = (min(room_length, room_width), max(room_length, room_width))
    if y > roll_width:
        return round(y * roll_width * roll_cost, 2)
    return round(x * roll_width * roll_cost, 2)
