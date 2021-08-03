T = int(input())

output = []
for t in range(T):
    R, C = list(map(int, input().strip().split()))
    x, y = list(map(int, input().strip().split()))

    corners = [[0, 0], [0, C - 1], [R - 1, 0], [R - 1, C - 1]]

    distances = []
    for corner in corners:
        dis = abs(x - corner[0]) + abs(y - corner[1])
        distances.append(dis)

    days = max(distances)
    output.append(days)


for x in output:
    print(x)
