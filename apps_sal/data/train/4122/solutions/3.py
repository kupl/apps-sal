def sc(s):
    return ''.join([e for e in s if {1: e.upper() in s, 0: e.lower() in s}[e.islower()]])
