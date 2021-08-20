test = int(input())
while test:
    t = input()
    h = int(t[0] + t[1])
    m = int(t[3] + t[4])
    h = h % 12
    if m == 60:
        m = 0
        h += 1
        if h > 12:
            h = h - 12
    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m
    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle, angle)
    a = angle
    b = int(angle)
    if a - b == 0:
        print(str(b) + ' degree')
    else:
        print(str(angle) + ' degree')
    test -= 1
