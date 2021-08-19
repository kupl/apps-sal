def meeting(rooms, need):
    if not need:
        return 'Game On'
    spare_chairs = []
    for (occupants, chairs) in rooms:
        available = min(need, max(chairs - len(occupants), 0))
        spare_chairs.append(available)
        need -= available
        if not need:
            return spare_chairs
    return 'Not enough!'
