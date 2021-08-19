def meeting(rooms, number):
    if number == 0:
        return 'Game On'
    chairs = [max(room[1] - len(room[0]), 0) for room in rooms]
    a = []
    i = 0
    while sum(a) < number and i < len(chairs):
        a.append(min(chairs[i], number - sum(a)))
        i += 1
    return a if sum(a) >= number else 'Not enough!'
