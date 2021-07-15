def correct_tail(body, tail):
    total = len(body)
    last_n = total - 1
    last = body[last_n]
    if last == tail:
        return True
    else:
        return False
