def correct_tail(body, tail):
#      sub = body.substr(len(body)-len(tail.length)
    if body.lower()[-1]==tail:
        return True
    else:
        return False
