def get_size(w, h, d):
    volume = h * w * d
    area = 2 * (w * h) + 2 * (w * d) + 2 * (h * d)
    res = []
    res.append(area)
    res.append(volume)
    return res


print(get_size(10, 10, 10))
