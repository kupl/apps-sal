def move(position, roll):
    if roll < 1 or roll > 6:
        return 'Error'
    else:
        new_position = position + roll * 2
        return new_position
