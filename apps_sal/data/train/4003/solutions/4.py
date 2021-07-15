def possible_positions(pos):
    moves = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
    res = []
    for m in moves:
        let = chr(ord(pos[0])+m[0])
        num = int(pos[1])+m[1]
        if let in "abcdefgh" and 0<num<9: res.append(let+str(num))
    return res
