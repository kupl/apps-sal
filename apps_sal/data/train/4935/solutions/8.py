def infected(s):
    totalinf = 0
    total = 0
    p = s.split('X')
    for item in p:
        if '1' in item:
            totalinf += len(item)
            total += len(item)
        else:
            total += len(item)
    return (float(100) * totalinf) / total if total != 0 else 0
