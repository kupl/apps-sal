def correct_tail(body, tail):
    sub = body.split()
    if sub[-1][-1] == tail:
        return True
    else:
        return False
