def correct_tail(body, tail):
    body.lower()
    tail.lower()
    a = body[-1]
    if a == tail:
        return True
    else:
        return False
