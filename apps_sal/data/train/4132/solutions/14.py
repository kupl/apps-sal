def correct_tail(body, tail):
    b = body[-1:].lower()
    c = tail[0].lower()
    if b == c:
        return True
    else:
        return False


correct_tail('Fox', 'x')
