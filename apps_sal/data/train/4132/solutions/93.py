def correct_tail(body, tail):
    sub = len(body)
    last = body[sub - 1]
    if last == tail:
        return True
    else:
        return False
