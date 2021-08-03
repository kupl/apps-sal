def my_crib(n):

    def line(n, l, m, r): return f'{ l }{ m*n }{ r }'.center(W)
    def topDoor(): return f'|{ ( "_"*half_1 ).center(W-2) }|'
    def door(b): return (b * half_1).join('||||')

    W, H, half_1 = 6 * n + 1, 4 * n + 1, 2 * n - 1

    return '\n'.join(line(2 * (n + i) - 1, *('/_\\' if i else '___')) if i <= 2 * n else
                     line(W - 2, *'| |') if i < 3 * n else
                     topDoor() if i == 3 * n else
                     door('_' if i == 4 * n else ' ') for i in range(H))
