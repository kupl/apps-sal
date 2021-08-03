for _ in range(int(input())):
    a, b, c, x, y, z = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and x == 0 and y == 0 and z == 0:
        print(0)
        continue
    ans = 0
    if a == 0 and b == 0 and c == 0:
        st = set((abs(x - a) % 2, abs(y - b) % 2, abs(z - c) % 2))
        if st == {0, 1}:
            ans = 1
        else:
            ans = 2
    else:
        if x == 0 and y == 0 and z == 0:
            st = set((abs(x - a) % 2, abs(y - b) % 2, abs(z - c) % 2))
            if st == {0, 1}:
                ans = 1
            else:
                ans = 2
        else:
            st = set((abs(x - a) % 2, abs(y - b) % 2, abs(z - c) % 2))
            if st == {0, 1}:
                ans = 1
    print(ans)
