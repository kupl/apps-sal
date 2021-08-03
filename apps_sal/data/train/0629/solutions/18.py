for _ in range(int(input())):
    r, g, b, m = map(int, input().split())
    R = max(list(map(int, input().split())))
    G = max(list(map(int, input().split())))
    B = max(list(map(int, input().split())))

    cur = [R, G, B]

    while m > 0:
        m -= 1
        index = cur.index(max(cur))
        cur[index] //= 2

    print(max(cur))
