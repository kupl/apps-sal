def controller(events):
    position, move, resume, positions = 0, 0, 0, []
    for event in events:
        if event == "P":
            if position == 0:
                move = 1
            elif position == 5:
                move = -1
            elif move:
                resume, move = move, 0
            else:
                move, resume = resume, 0
        elif event == "O":
            move = -move
        position = min(5, max(0, position + move))
        if position == 0 or position == 5:
            move = 0
        positions.append(str(position))
    return "".join(positions)
