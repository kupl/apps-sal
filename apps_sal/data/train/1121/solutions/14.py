# cook your dish here
for i in range(int(input())):
    t = input()
    l = t.split(":")
    l[0] = int(l[0])
    l[1] = int(l[1])
    if l[0] >= 12:
        l[0] = l[0] - 12
    m = l[1] * 6
    h = l[0] * 30 + l[1] * 0.5
    if abs(m - h) > 180:
        ans = 360 - abs(m - h)
    else:
        ans = abs(m - h)

    print("{0:.2f}".format(ans).rstrip("0").rstrip("."), "degree")
