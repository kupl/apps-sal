def meeting(rooms, number):
    if number == 0:
        return 'Game On'
    chairs = []
    for i in rooms:
        if sum(chairs) == number:
            return chairs
        if i[-1] - len(i[0]) <= 0:
            chairs.append(0)
        elif sum(chairs) + i[1] - len(i[0]) >= number:
            chairs.append(number - sum(chairs))
        else:
            chairs.append(i[-1] - len(i[0]))
    if sum(chairs) == number:
        return chairs
    if sum(chairs) < number:
        return 'Not enough!'
