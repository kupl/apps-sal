def correct_tail(body, tail):
    sub = body[len(body)-len(tail)]
    return True if (sub==tail) else False
