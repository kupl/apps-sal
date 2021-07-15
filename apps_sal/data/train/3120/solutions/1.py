def meeting(rooms, number):
    if number == 0:
        return 'Game On'
    result = []
    for taken, n in rooms:
        available = n - len(taken)
        chairs = min(max(available, 0), number)
        number -= chairs
        result.append(chairs)
        if not number:
            return result
    return 'Not enough!'

