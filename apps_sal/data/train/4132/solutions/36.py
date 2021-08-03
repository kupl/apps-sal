def correct_tail(body, tail):
    for char in body:
        if body[-1] == tail:
            return True

        else:
            return False
