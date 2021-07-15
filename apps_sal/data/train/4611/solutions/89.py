def animals(h,l):
    """
    Count cows and chickens
    """
    co = (l-2*h)//2
    ch = h - co
    return 'No solutions' if ch < 0 or co < 0 or h < 0 or l % 2 != 0 or l < 0  else (ch,co)
