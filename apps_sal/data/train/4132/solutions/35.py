def correct_tail(body, tail):
    #sub = body.substr(len(body)-len(tail.length)
    if body.endswith(tail):
        return True
    else:
        return False
