for _ in range(int(input())):
    (x, y, n) = map(int, input().split())
    n += 1
    ans = 0
    are_same = True
    for j in range(29, -1, -1):
        if are_same:
            if x & 1 << j != y & 1 << j:
                for k in range(29, -1, -1):
                    if j > k:
                        if n & 1 << k:
                            if n & 1 << j == x & 1 << j:
                                ans += 1 << k
                    elif j == k:
                        if n & 1 << k:
                            if x & 1 << j == 0:
                                ans += 1 << k
                    elif n & 1 << k:
                        ans += 1 << k - 1
        if x & 1 << j != y & 1 << j:
            are_same = False
    print(ans)
