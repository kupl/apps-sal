def correct_tail(body, tail):
    sub = body[len(body) - 1:body.rfind(tail) + 1]
    if tail == sub:
        return True
    else:
        return False
