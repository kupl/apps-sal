def increment_string(s):
    c = s.rstrip('0123456789')
    n = s[len(c):]
    if n=='':
        return s+'1'
    else:
        return c+str(int(n)+1).zfill(len(n))
