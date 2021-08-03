def move(position, roll):
    if roll > 0:
        position += roll * 2
    elif roll < 0:
        position -= roll * 2
    else:
        position = position
    return position
