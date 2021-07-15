def correct_tail(body, tail):
    subs = body[len(body)-len(tail)]
    if subs == tail:
        return True
    else:
        return False
