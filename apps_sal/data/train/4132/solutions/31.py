def correct_tail(body, tail):
    return True if body[len(body)-len(tail):len(body)] == tail else False
