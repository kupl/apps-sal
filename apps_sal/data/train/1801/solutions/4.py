def pairs(code):
    opening = []
    matching = {}

    for i, c in enumerate(code):
        if c == "[":
            opening.append(i)
        elif c == "]":
            j = opening.pop()
            matching[i] = j
            matching[j] = i
    assert not opening
    return matching


def interpreter(code, iterations, width, height):
    matching = pairs(code)

    x = 0
    y = 0
    canvas = [[0 for _ in range(width)] for _ in range(height)]

    index = 0
    iterations_done = 0

    while iterations_done < iterations:
        try:
            c = code[index]
        except IndexError:
            break
        iterations_done += 1
        if c == "n":
            y -= 1
            y %= height
            index += 1
        elif c == "s":
            y += 1
            y %= height
            index += 1
        elif c == "w":
            x -= 1
            x %= width
            index += 1
        elif c == "e":
            x += 1
            x %= width
            index += 1
        elif c == "*":
            canvas[y][x] ^= 1
            index += 1
        elif c == "[":
            if canvas[y][x] == 0:
                index = matching[index]
            index += 1
        elif c == "]":
            if canvas[y][x] != 0:
                index = matching[index]
            index += 1
        else:
            iterations_done -= 1
            index += 1

    return "\r\n".join("".join(map(str, row)) for row in canvas)
