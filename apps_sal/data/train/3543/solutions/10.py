def increment_string(s):
    from re import findall as fa
    return (s.replace((fa('(\d+)', s))[-1], str(int((fa('(\d+)', s))[-1]) + 1).rjust(len((fa('(\d+)', s))[-1]), '0')) if (fa('(\d+)', s)) else s + '1')
