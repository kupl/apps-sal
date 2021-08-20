test_case = int(input())
while test_case:
    n = int(input())
    points = []
    total_points = 4 * n - 1
    for _ in range(total_points):
        points.append(list(map(int, input().strip().split())))
    xor_x = 0
    xor_y = 0
    for p in points:
        xor_x ^= p[0]
        xor_y ^= p[1]
    print(xor_x, xor_y)
    test_case -= 1
