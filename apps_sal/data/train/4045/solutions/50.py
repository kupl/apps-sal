def number(lines):
    count = 1
    out = []
    for i in lines:
        out.append(str(count) + ": " + i)
        count += 1
    return out
