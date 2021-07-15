def move(position, roll):
    return roll * 2 if position == 0 else (position + roll) * 2 - position
