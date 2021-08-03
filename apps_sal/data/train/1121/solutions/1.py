# cook your dish here
T = int(input())
for _ in range(T):
    s = input()
    h, m = int(s[:2]), int(s[3:])
    if h > 12:
        h -= 12
    if h == 12:
        h = 0
    if m == 60:
        m = 0
        h += 1
        if h > 12:
            h -= 12
    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m
    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle, angle)
    my_st = str(angle)
    if my_st[-1] == '0':
        print(int(angle), 'degree')
    else:
        print(angle, 'degree')
