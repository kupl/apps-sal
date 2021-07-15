def correct_tail(body, tail):
    index = [letter for letter in body]
    if index[-1] == tail:
        return True
    else:
        return False
