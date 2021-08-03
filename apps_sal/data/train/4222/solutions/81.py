def get_size(w, h, d):
    # your code here
    result = []
    vol = w * h * d
    area = (w * d + h * d + h * w) * 2
    result.append(area)
    result.append(vol)
    return result
