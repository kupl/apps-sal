def cost_of_carpet(room_length, room_width, roll_width, roll_cost):
    if room_length > roll_width < room_width or room_length * room_width <= 0:
        return 'error'
    if room_length <= roll_width >= room_width:
        side = min(room_length, room_width)
    else:
        side = max(room_length, room_width)
    return round(side * roll_width * roll_cost, 2)
