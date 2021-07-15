def shortest_to_char(s, c):
    if not c: return []
    l = []
    for i,x in enumerate(s):
        a,b = s[i:].find(c), s[:i+1][::-1].find(c)
        if a != -1:
            a = abs(i-i + a)
        else: a = float('inf')
        if b != -1:
            b = s[:i+1][::-1].find(c)
        else: b = float('inf')
        get_min = min(a,b)
        if get_min != float('inf'):
            l.append(get_min)
    return l
