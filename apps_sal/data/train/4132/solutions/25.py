def correct_tail(body, tail):
    sub = len(body)
    sub = body[::-sub]
    if sub == tail:
        return True
    else:
        return False
