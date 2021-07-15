import re

pos = [0, 0]    # pos-x is down, pos-y is right
direction = 0   # 0=up, 1=right, 2=down, 3=left

def i_am_here(path):
    commands = list(re.findall("(\d+|[lrLR])", path))
    nonlocal direction, pos
    for command in commands:
        if command.isdigit():
            steps = int(command)
            if direction % 2 == 0:
                pos[0] += steps if direction == 2 else -steps
            else:
                pos[1] += steps if direction == 1 else -steps
        elif command == "r":
            direction = (direction + 1) % 4
        elif command == "l":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 2) % 4
    return pos
