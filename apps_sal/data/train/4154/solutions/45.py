def is_triangle(a, b, c):
    out = []
    out.append(a)
    out.append(b)
    out.append(c)
    out.sort()
    if out[2] >= out[0] + out[1]:
        return False
    else:
        return True
