def increment_string(strng):
    s = strng.rstrip('0123456789')
    n = strng[len(s):]
    if n is '':
        return s + '1'
    else:
        n_ = int(n) + 1
        d = len(str(n)) - len(str(n_))
        if d != 0:
            return s + d * '0' + str(n_)
        else:
            return s + str(n_)
