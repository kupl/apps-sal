def list_depth(l):
    a = [0]
    for i in str(l):
        if i == '[':
            a.append(a[-1] + 1)
        if i == ']':
            a.append(a[-1] - 1)
    return max(a)
