def get_size(w, h, d):
    ans = []
    surface = 2 * ((w * h) + (d * h) + (w * d))
    volume = w * h * d
    ans.append(surface)
    ans.append(volume)
    return ans
