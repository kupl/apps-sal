t = int(input())
for i in range(t):
    s = input() + 'R'
    mx = -float('inf')
    cur = 0
    while s.find('R', cur) != -1:
        nxt = s.find('R', cur)
        d = nxt - cur
        if d > mx:
            mx = d
        cur = nxt + 1
    print(mx + 1)
