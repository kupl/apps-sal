for zz in range(int(input())):
    (n, x) = list(map(int, input().split()))
    z = list(str(input()))
    (c1, c2) = (z[0], z[2])
    ans1 = x if c1 == 'L' else n + 1 - x
    ans2 = c2 if ans1 % 2 == 1 else 'E' if c2 == 'H' else 'H'
    print(ans1, ans2)
