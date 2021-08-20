def correct_tail(body, tail):
    index = len(body) - 1
    last_letter = body[index]
    if last_letter == tail:
        return True
    else:
        return False
