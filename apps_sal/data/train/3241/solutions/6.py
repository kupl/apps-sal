def buy_newspaper(s1, s2):
    if not all((i in s1 for i in s2)):
        return -1
    (copy, i) = (s1, 1)
    while True:
        pos = [float('-inf')]
        for k in s2:
            t = next((o for (o, p) in enumerate(s1) if p == k and o > pos[-1]), -1)
            if t == -1:
                break
            pos.append(t)
        else:
            return i
        s1 += copy
        i += 1
