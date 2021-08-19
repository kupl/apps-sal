def center_of(chars):
    center = ''
    n = len(chars)
    if n == 0:
        return center
    elif n % 2 == 0:
        n //= 2
    pos = []
    for i in range(n):
        pos.append(2 * i * (i + 1) % len(chars))
    for num in pos:
        center += chars[num]
    for i in range(len(center) // 2):
        test = center[:i + 1]
        if center == test * (len(center) // len(test)):
            center = test
            break
    return center
