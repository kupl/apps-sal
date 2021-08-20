def increment_string(s):
    if s and s[-1].isdigit():
        n = s[len(s.rstrip('0123456789')):]
        return s[:len(s) - len(n)] + '%0*d' % (len(n), int(n) + 1)
    return s + '1'
