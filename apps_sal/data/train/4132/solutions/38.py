def correct_tail(body, tail):
    if isinstance(body, str) and isinstance(tail, str) and len(tail) > 0:
        if body[-1] == tail:
            return True
    return False
