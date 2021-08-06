for cas in range(eval(input())):
    n, sx, sy, ex, ey, bx, by = list(map(int, input().strip().split()))
    print(abs(sx - ex) + abs(sy - ey) + 2 * ((sx == ex or sy == ey)
     and min(sx, ex) <= bx <= max(sx, ex)
        and min(sy, ey) <= by <= max(sy, ey)
    ))
