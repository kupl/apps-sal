def modes(data):
    (most, l, length) = (0, [], len(data))
    for x in set(data):
        res = data.count(x)
        if most < res:
            most = res
            l = []
            l.append(x)
            length = len(data) - most
        elif most == res:
            l.append(x)
            length -= most
    return sorted(l) if length else []
