def list_depth(l):
    a = str(l)
    z = 0
    for i in a[::-1]:
        if i == ']':
            z += 1
        elif i == '[':
            break
    return z
