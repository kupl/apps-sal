def meeting(rooms):
    return next((i for i, x in enumerate(rooms) if x == 'O'), 'None available!')
