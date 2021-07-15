def correct_tail(body, tail):
    x = body.split()
    y = body[-1]
    if y == tail:
        return True
    else:
        return False
