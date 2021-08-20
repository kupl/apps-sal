def meeting(rooms):
    return [o for (o, v) in enumerate(rooms) if v == 'O'][0] if 'O' in rooms else 'None available!'
