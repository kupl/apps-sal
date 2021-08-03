x = 0
y = 0
heading = 0


def plus(cpl1, cpl2, factor):
    return [cpl1[0] + cpl2[0] * factor, cpl1[1] + cpl2[1] * factor]


headings = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def change_heading(heading, character):
    if character == "l":
        return (heading + 1) % 4
    if character == "r":
        return (heading - 1) % 4
    if character == "L":
        return (heading - 2) % 4
    if character == "R":
        return (heading - 2) % 4


def i_am_here(path):
    nonlocal x
    nonlocal y
    nonlocal heading
    buffnum = ""
    i = 0
    while i < len(path):
        character = path[i]
        if '0' <= character <= '9':
            buffnum += character
        else:
            if buffnum != "":
                [x, y] = plus([x, y], headings[heading], int(buffnum))
                buffnum = ""
            heading = change_heading(heading, character)
        i += 1
    if buffnum != "":
        [x, y] = plus([x, y], headings[heading], int(buffnum))
    return [x, y]
