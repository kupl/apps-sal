def correct_tail(body, tail):
    sub = len(body) - len(tail)
    if body[-1] == tail:
        return True
    else:
        return False
