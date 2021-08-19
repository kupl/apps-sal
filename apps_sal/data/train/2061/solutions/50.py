T = int(input())
for t in range(T):
    (ax, ay, bx, by, cx, cy) = [int(i) for i in input().split()]
    ([ax, ay], [bx, by], [cx, cy]) = sorted([[ax, ay], [bx, by], [cx, cy]], key=lambda x: x[1])
    ([ax, ay], [bx, by], [cx, cy]) = sorted([[ax, ay], [bx, by], [cx, cy]], key=lambda x: x[0])
    if [ax, ay, bx, by, cx, cy] == [0, 0, 0, 1, 1, 0]:
        print(0)
        continue
    elif [ax, ay, bx, by, cx, cy] == [0, 1, 1, 0, 1, 1]:
        print(1)
        continue
    if [bx, by - 1] == [ax, ay] and [cx - 1, cy] == [ax, ay]:
        g = [bx + cx - 1, by + cy - 1]
    if [bx, by - 1] == [ax, ay] and [cx - 1, cy - 1] == [ax, ay]:
        g = [ax + cx - 1, ay + cy]
    if [bx - 1, by + 1] == [ax, ay] and [cx - 1, cy] == [ax, ay]:
        g = [ax + bx, ay + by]
    if [bx - 1, by] == [ax, ay] and [cx - 1, cy - 1] == [ax, ay]:
        g = [ax + cx, ay + cy - 1]
    ans = max([abs(x) for x in g]) + (g[0] == g[1])
    print(ans)
