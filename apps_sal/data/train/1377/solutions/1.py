for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    s = (a + b) / 2
    t = (c + d) / 2
    if s > t:
        print(s - t, "DEGREE(S) ABOVE NORMAL")
    else:
        print(t - s, "DEGREE(S) BELOW NORMAL")
