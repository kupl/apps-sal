for _ in range(int(input())):
    s = input()
    lst = s.split(':')
    h = int(lst[0])
    m = int(lst[1])
    h = h % 12
    h_angle = h * 30 + m * 0.5
    m_angle = (m * 30) / 5
    val = abs(h_angle - m_angle)
    ans = min(360 - val, val)
    if ans == int(ans):
        print(int(ans), 'degree')
    else:
        print(ans, 'degree')
