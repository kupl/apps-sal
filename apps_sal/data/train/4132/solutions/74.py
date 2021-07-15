def correct_tail(body, tail):
    list = body.split()
    sub = list[0][-1]
    if sub == tail:
        return True
    else:
        return False
