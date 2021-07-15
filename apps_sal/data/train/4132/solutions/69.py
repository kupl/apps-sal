def correct_tail(body, tail):
    i = len(body)-2
    sub = body[:i:-1]
    print(sub)
    if sub == tail:
        return True
    else:
        return False
