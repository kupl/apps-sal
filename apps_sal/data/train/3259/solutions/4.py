def tv_remote(words):
    pad = ["abcde123", "fghij456", "klmno789", "pqrst.@0", "uvwxyz_/", "S "]
    index = {c: (x, y) for x, lst in enumerate(pad) for y, c in enumerate(lst)}
    res = 0
    pos = (0, 0)
    caps = False
    for char in words:
        if char.isalpha() and (char.isupper() != caps):
            res += (abs(pos[0] - index["S"][0]) + abs(pos[1] - index["S"][1])) + 1
            pos = index["S"]
            caps = not caps
        
        char = char.lower()
        res += (abs(pos[0] - index[char][0]) + abs(pos[1] - index[char][1])) + 1
        pos = index[char]
    return res
