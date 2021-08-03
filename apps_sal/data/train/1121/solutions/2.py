for t in range(int(input())):
    a = input().split(":")
    hr, min = int(a[0]), int(a[1])
    if hr >= 12:
        hr -= 12
    m_angle = int(min / 5) * 30
    h_angle = hr * 30 + min / 2
    if h_angle - int(h_angle) == 0:
        h_angle = int(h_angle)
    if abs(m_angle - h_angle) <= 180:
        print(abs(m_angle - h_angle), "degree")
    else:
        print(360 - abs(m_angle - h_angle), "degree")
