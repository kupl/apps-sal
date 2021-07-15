from_pos = lambda s: (ord(s[0])-65, int(s[1])-1)
to_pos = lambda i,j: f"{chr(i+65)}{j+1}"

def available_moves(position):
    # That part is always just annoying
    if not (isinstance(position, str)
            and len(position) == 2
            and position[0] in "ABCDEFGH"
            and position[1] in "12345678"): return []
    
    (x, y), res = from_pos(position), []
    for k,l in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
        i, j = y+k, x+l
        while 0 <= i < 8 and 0 <= j < 8:
            res.append(to_pos(j, i))
            i, j = i+k, j+l
    return sorted(res)
