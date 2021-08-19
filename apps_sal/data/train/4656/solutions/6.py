def center_of(chars):
    size = len(chars)
    if size == 0:
        return ""

    size = len(chars)
    center_calc = size * 4
    center = ''
    index_large = 0
    for n in range(center_calc):
        index_large += n * 4
        index = index_large % size
        center += chars[index]

    # print(center)

    for n in range(1, center_calc):
        if center[:n] == center[n:2 * n] and center[n:2 * n] == center[2 * n:3 * n] and center[2 * n:3 * n] == center[3 * n:4 * n]:
            return center[:n]

    return(center)
