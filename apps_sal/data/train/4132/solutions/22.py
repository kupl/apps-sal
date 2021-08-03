def correct_tail(body, tail):
    i = len(body) - len(tail)
    if body[i] == tail:
        return True
    else:
        return False
