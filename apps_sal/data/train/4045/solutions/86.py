def number(lines):
    _ = 1
    for i in range(0, len(lines)):
        lines[i] = str(_) + ": " + str(lines[i])
        _ += 1

    return lines
