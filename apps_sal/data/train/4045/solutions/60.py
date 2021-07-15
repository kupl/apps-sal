def number(lines):
    if len(lines) == 0:
        return []
    else:
        count = 1
        for x in lines:
            lines[count-1] = str(count) + ": " + x
            count += 1
        return lines
