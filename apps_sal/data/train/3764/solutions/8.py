def arbitrate(s,n):
    return ''.join('1' if v=='1' and '1' not in s[:i] else '0' for i,v in enumerate(s))
