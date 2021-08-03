def move(position, roll):
    if roll < 7:
        return position + roll * 2
