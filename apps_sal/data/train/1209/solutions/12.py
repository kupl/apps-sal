def __starting_point():
    for t in range(int(input())):
        yes = False
        v1, t1, v2, t2, v3, t3 = map(int, input().split())
        if t1 <= t3 <= t2:
            yes = (t2 - t3) * v3 <= v1 * (t2 - t1) and (t3 - t1) * v3 <= v2 * (t2 - t1)
        print("YES" if yes else "NO")


__starting_point()
