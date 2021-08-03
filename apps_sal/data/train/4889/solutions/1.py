def max_hexagon_beam(n: int, seq: tuple):
    """Compute maximum sum along "beams" of an hexagon

            _-'-_   _-'-_                 o--- +i
          .'     '.'     '.               |
          |0,-1,1 |1,-1,0 |               '
        _-'-_   _-'-_   _-'-_            +j
      .'     '.'     '.'     '.     
      |-1,0,1 | q,r,s | 1,0,-1|     +s         +q
      '-_   _-'-_   _-'-_   _-'       '-_   _-'
         '.'     '.'     '.'             'o'
          |-1,1,0 | 0,1,-1|               |
          '-_   _-'-_   _-'               '
             '.'     '.'                 +r

    hex->grid: i = r+n-1
               j = q+n-1+min(r,0)

    grid->hex: r = i+1-n
               q = j+1-n-min(r,0)
               s = -q-r

    beams: 1-n-min(r,0) <= q,s <= n-1-max(r,0)  etc.
    """

    i = 0
    grid = []
    length = len(seq)

    for r in range(1 - n, n):
        grid.append([])
        for q in range(1 - n - min(r, 0), n - max(r, 0)):
            grid[r + n - 1].append(seq[i % length])
            i += 1

    return max((
        max(sum(grid[r + n - 1][q + n - 1 + min(r, 0)] for r in range(1 - n - min(q, 0), n - max(q, 0))) for q in range(1 - n, n)),
        max(sum(grid[r + n - 1][-s - r + n - 1 + min(r, 0)] for s in range(1 - n - min(r, 0), n - max(r, 0))) for r in range(1 - n, n)),
        max(sum(grid[-q - s + n - 1][q + n - 1 + min(-q - s, 0)] for q in range(1 - n - min(s, 0), n - max(s, 0))) for s in range(1 - n, n)),
    ))
