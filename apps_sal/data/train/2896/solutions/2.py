def cost_of_carpet(room_length, room_width, roll_width, roll_cost):
    if room_length > roll_width and room_width > roll_width or not room_length * room_width * roll_width:
        return 'error'
    [a, b] = sorted([room_length, room_width])
    if room_length <= roll_width and room_width <= roll_width:
        return round(roll_width * a * roll_cost, 2)
    return round(b * roll_width * roll_cost, 2)
