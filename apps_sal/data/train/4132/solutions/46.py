def correct_tail(body, tail):
    sub = body[len(body) - 1]
    if sub == tail[len(tail) - 1]:
        return True
    else:
        return False
