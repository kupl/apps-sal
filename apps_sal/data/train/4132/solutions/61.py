def correct_tail(body, tail):
    #sub = body.substr(len(body)-len(tail.length))
    sub = body[len(body) - 1]
    if sub == tail:
        return True
    else:
        return False
