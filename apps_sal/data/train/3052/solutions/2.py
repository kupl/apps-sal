def remove(s):
    end_i = len(s.rstrip('!'))
    return s[:end_i].replace('!', '') + s[end_i:]
