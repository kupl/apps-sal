def tetris(arr) -> int:
    bd, lines = [0]*9, 0
    for n,d,m in arr:
        i = int(m)*(-1)**(d=='R')
        bd[i] += int(n)
        if bd[i]>29:
            h = min(bd)
            if bd[i]-h>29: break
            lines += h
            bd = [v-h for v in bd]
    lines += min(bd)
    return lines
