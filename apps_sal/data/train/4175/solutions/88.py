repeater = lambda s, n: s + repeater(s,n-1) if n > 0 else ''
