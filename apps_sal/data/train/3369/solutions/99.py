def move(position, roll):
    if (roll >= 1) and (roll <= 6):
        position += (roll * 2)
        return position
