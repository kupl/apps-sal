def promenade(choices):
    last_left = [1,0]
    last_right = [0,1]
    out = [1,1]
    for choice in choices:
        if choice is 'L':
            last_left = out.copy()
            out[0] += last_right[0]
            out[1] += last_right[1]
        else:
            last_right = out.copy()
            out[0] += last_left[0]
            out[1] += last_left[1]
    return tuple(out)

