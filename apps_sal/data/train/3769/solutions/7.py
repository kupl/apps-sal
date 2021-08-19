def execute(code):
    (R, r, c, dr, dc) = ({(0, 0)}, 0, 0, 0, 1)
    D = {(1, 0): {'R': (0, -1), 'L': (0, 1)}, (-1, 0): {'R': (0, 1), 'L': (0, -1)}, (0, 1): {'R': (1, 0), 'L': (-1, 0)}, (0, -1): {'R': (-1, 0), 'L': (1, 0)}}
    for cmd in code.replace('R', ' R').replace('L', ' L').replace('F', ' F').strip().split():
        (cmd, n) = (cmd[:1], int(cmd[1:]) if cmd[1:] else 1)
        for _ in range(n):
            if cmd in 'RL':
                (dr, dc) = D[dr, dc][cmd]
            else:
                (r, c) = (r + dr, c + dc)
                R.add((r, c))
    mnr = min((r for (r, _) in R))
    mnc = min((c for (_, c) in R))
    R = {(r - mnr, c - mnc) for (r, c) in R}
    mxr = max((r for (r, _) in R))
    mxc = max((c for (_, c) in R))
    return '\r\n'.join((''.join((' *'[(r, c) in R] for c in range(mxc + 1))) for r in range(mxr + 1)))
