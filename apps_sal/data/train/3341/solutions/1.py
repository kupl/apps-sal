def pop_shift(s):
    (il, ir) = (len(s) // 2, (len(s) + 1) // 2)
    return [s[:ir - 1:-1], s[:il], s[il:ir]]
