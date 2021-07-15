def meeting(rooms, need):
    if need == 0:
        return "Game On"
    take = []
    for people, seat in rooms:
        take.append(min(need, max(0, seat - len(people))))
        need -= take[-1]
        if need == 0:
            return take
    return "Not enough!"
