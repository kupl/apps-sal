def cost_of_carpet(room_length, room_width, roll_width, roll_cost):
    if roll_width < min(room_length, room_width):
        return 'error'
    elif  room_length == 0 or room_width ==0:
         return "error"
    cost_1 = roll_width*room_length*roll_cost if roll_width >= room_width else float('inf')
    cost_2 = roll_width*room_width*roll_cost if roll_width >= room_length else float('inf')
    return round(min(cost_1, cost_2), 2)
     
   

    

