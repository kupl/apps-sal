def move(position, roll):
    i = 0
    for i in range(roll):
        position += 2
    return position


move(0, 4)
