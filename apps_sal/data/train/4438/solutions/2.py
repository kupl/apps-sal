def middle_point(*coords):
    return sorted(((coords[i * 3:i * 3 + 3], i + 1) for i in range(3)))[1][-1]
