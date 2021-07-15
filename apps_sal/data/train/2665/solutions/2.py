def meeting(rooms):
    return next((i for i, r in enumerate(rooms) if r == 'O'), 'None available!')
