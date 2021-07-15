def meeting(rooms, number):
    if not number:
        return 'Game On'
    accumulate = []
    for r in rooms:
        available = max(r[1] - len(r[0]), 0)
        take = min(number, available)
        accumulate.append(take)
        number -= take
        if number == 0:
            return accumulate
    return 'Not enough!'
