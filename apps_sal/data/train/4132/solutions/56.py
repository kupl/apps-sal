def correct_tail(body, tail):
    bool = False
    last = len(body)
    last = last - 1
    if body[last] == tail:
        bool = True
    return bool
