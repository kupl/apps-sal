t = int(input())
for z in range(t):
    d = list(input().split())
    front, back, left, right, top, bottom = d[0], d[1], d[2], d[3], d[4], d[5]
    if (front == left or front == right) and (front == top or front == bottom):
        print('YES')
    elif (back == left or back == right) and (back == top or back == bottom):
        print('YES')
    else:
        print('NO')
