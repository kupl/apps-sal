S = input()
T = input()
s_rui = [0]
t_rui = [0]
for s in S:
    if s == 'A':
        s_rui.append(s_rui[-1] + 1)
    else:
        s_rui.append(s_rui[-1] + 2)
for t in T:
    if t == 'A':
        t_rui.append(t_rui[-1] + 1)
    else:
        t_rui.append(t_rui[-1] + 2)
for _ in range(int(input())):
    (a, b, c, d) = map(int, input().split())
    ss = s_rui[b] - s_rui[a - 1]
    tt = t_rui[d] - t_rui[c - 1]
    if ss % 3 == tt % 3:
        print('YES')
    else:
        print('NO')
