# cook your dish here
import math
t = int(input())
for i in range(t):
    h, m = input().split(':')
    h_pos = int(h) * 30
    if int(h) >= 12:
        h_pos = (int(h) - 12) * 30
    m_pos = int(m) * 6
    h_curpos = h_pos + int(m) * 0.5
    ang = abs(h_curpos - m_pos)
    ang1 = 360 - ang
    fin_ang = min(ang, ang1)
    if math.floor(fin_ang) == fin_ang:
        print(int(fin_ang), 'degree')
    else:
        print(float(fin_ang), 'degree')
