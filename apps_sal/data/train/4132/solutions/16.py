def correct_tail(body, tail):
    n = len(body)
    if body[n - 1] == tail[0]:
        return True
    else:
        return False
