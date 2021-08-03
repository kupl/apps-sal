def correct_tail(body, tail):
    b = [str(x) for x in body[::-1]]
    t = [str(y) for y in tail[::-1]]

    return True if b[0] == t[0] else False
