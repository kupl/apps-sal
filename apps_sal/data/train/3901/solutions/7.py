def check_digit(s, t, p, q):
    if t < p:

        return True if str(q) in str(s)[t:p + 1] else False
    return True if str(q) in str(s)[p:t + 1] else False
