for i in range(int(input())):
    (r, c) = list(map(int, input().split()))
    (y, x) = list(map(int, input().split()))
    s1 = x + y
    s2 = y + (c - x - 1)
    s3 = c - x - 1 + (r - y - 1)
    s4 = x + (r - y - 1)
    print(max(s1, s2, s3, s4))
