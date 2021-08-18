BLANK = " "
FILLCHAR = "*"


def pad_mtx(M, side="e"):
    """
    Pads matrix with row or column of blank chars depending on side keyword
    """
    if side == "w":
        for i in range(len(M)):
            M[i] = [BLANK] + M[i][::1]
    elif side == "e":
        for i in range(len(M)):
            M[i] += [BLANK]
    elif side == "n":
        M.insert(0, [BLANK for _ in range(len(M[0]))])
    elif side == "s":
        M.append([BLANK for _ in range(len(M[0]))])


def move(mtx, pos, drxn):
    if drxn == "e":
        pos[1] += 1
    elif drxn == "w":
        pos[1] -= 1
    elif drxn == "s":
        pos[0] += 1
    elif drxn == "n":
        pos[0] -= 1
    else:
        raise ValueError("Direction unrecognized.")

    try:
        if any(x < 0 for x in pos):
            raise ValueError
        else:
            mtx[pos[0]][pos[1]] = FILLCHAR
    except Exception:
        pad_mtx(mtx, side=drxn)
        if drxn == "n":
            pos[0] += 1
        if drxn == "w":
            pos[1] += 1
        mtx[pos[0]][pos[1]] = FILLCHAR


def rotate(current, turn):
    directions = ["e", "s", "w", "n"]
    turns = {"L": -1, "R": 1}
    idx = directions.index(current)
    return directions[(idx + turns[turn]) % len(directions)]


def execute(code):
    directions = ["e", "s", "w", "n"]
    path = [[FILLCHAR]]
    pos = [0, 0]
    drxn = "e"
    i = 0
    while i < len(code):
        num = ""
        if i != len(code) - 1 and code[i + 1].isdigit():
            j = i + 1
            while j < len(code) and code[j].isdigit():
                num += code[j]
                j += 1
            for _ in range(int(num)):
                if code[i] in "LR":
                    drxn = rotate(drxn, code[i])
                elif code[i] == "F":
                    move(path, pos, drxn)
                else:
                    break

        elif code[i] == "F":
            move(path, pos, drxn)
        elif code[i] in "LR":
            drxn = rotate(drxn, code[i])
        i += 1
    return "\r\n".join("".join(row) for row in path)
