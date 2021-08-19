def meeting(rooms):
    for (num, status) in enumerate(rooms):
        if status == 'O':
            return num
    return 'None available!'
