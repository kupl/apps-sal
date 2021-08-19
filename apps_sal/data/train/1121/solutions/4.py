def calcAngle(h, m):
    if h < 0 or m < 0 or h > 12 or (m > 60):
        print('Wrong input')
    if h == 12:
        h = 0
    if m == 60:
        m = 0
        h += 1
        if h > 12:
            h = h - 12
    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m
    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle, angle)
    if angle.is_integer():
        return int(angle)
    else:
        return angle


def __starting_point():
    T = int(input())
    for i in range(T):
        t = input()
        h = int(t.split(':')[0]) % 12
        m = int(t.split(':')[1])
        print(calcAngle(h, m), 'degree')


__starting_point()
