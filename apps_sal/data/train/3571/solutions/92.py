def is_divisible(wall_length, pixel_size):
    t = True
    f = False
    text = wall_length % pixel_size
    if text == 0:
        ans = t
    else:
        ans = f
    return ans
