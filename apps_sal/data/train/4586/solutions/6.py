def tv_remote(word):
    pad = ["abcde123", "fghij456", "klmno789", "pqrst.@0", "uvwxyz_/"]
    index = {c: (x, y) for x, lst in enumerate(pad) for y, c in enumerate(lst)}
    res = 0
    pos = (0, 0)
    for char in word:
        res += (abs(pos[0] - index[char][0]) + abs(pos[1] - index[char][1])) + 1
        pos = index[char]
    return res
