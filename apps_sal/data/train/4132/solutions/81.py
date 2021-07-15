def correct_tail(body, tail):
    print(body)
    print(tail)
    #b=len(body[-1:])
    #print(b)
    #sub = body.substr(len(body)-len(tail.length)
    if body[-1:] == tail:
        return True
    else:
        return False
