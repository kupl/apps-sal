def mix(s1, s2):
    s = []
    lett = "abcdefghijklmnopqrstuvwxyz"
    for ch in lett:
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) >= 2:
            if val1 > val2: s.append("1:"+val1*ch)
            elif val1 < val2: s.append("2:"+val2*ch)
            else: s.append("=:"+val1*ch)
            
    s.sort()
    s.sort(key=len, reverse=True)
    return "/".join(s)

