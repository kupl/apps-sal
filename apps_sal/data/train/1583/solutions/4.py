T = int(input())
for i in range(T):
    (n, sx, sy, ex, ey, bx, by) = list(map(int, input().split()))
    if sx != ex and sy != ey:
        a = abs(sx - ex) + abs(sy - ey)
        print(a)
    elif sx == ex:
        if ex == bx and (by - sy) * (ey - by) > 0:
            print(abs(sy - ey) + 2)
        else:
            print(abs(sy - ey))
    elif ey == by and (bx - sx) * (ex - bx) > 0:
        print(abs(sx - ex) + 2)
    else:
        print(abs(sx - ex))
