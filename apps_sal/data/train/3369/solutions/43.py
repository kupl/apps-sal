def move(position, roll, moves=2):
    return move(position, roll, moves - 1) + roll if moves else position
