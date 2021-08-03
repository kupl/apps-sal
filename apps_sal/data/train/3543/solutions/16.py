def increment_string(s):
    if s == '' or not s[-1].isdigit():
        return s + '1'

    n = s[len(s.rstrip('0123456789')):]
    return s[:len(s) - len(n)] + '%0*d' % (len(n), int(n) + 1)
