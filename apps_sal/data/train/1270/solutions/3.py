def min_boxes(k, boxes):
    if len(boxes) == 1:
        return -1
    sum_ = sum(boxes)
    boxes = sorted(boxes, reverse=True)
    n = len(boxes)
    if sum_ < 2 * k:
        return -1
    elif boxes[0] >= k:
        B = boxes[1]
        if B >= k:
            return 2
        for i in range(2, n):
            B += boxes[i]
            if B >= k:
                return i + 1
        return -1
    table = [[False for _ in range(2 * k)] for _ in range(n + 1)]
    for i in range(n + 1):
        table[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, 2 * k):
            if boxes[i - 1] > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = table[i - 1][j] or table[i - 1][j - boxes[i - 1]]
    sum_till_here = 0
    for i in range(1, n + 1):
        sum_till_here += boxes[i - 1]
        for j in range(k, sum_till_here - k + 1):
            if table[i][j]:
                return i
    return -1


def __starting_point():
    test_cases = int(input())
    while test_cases:
        (n, k) = map(int, input().split())
        boxes = list(map(int, input().split()))
        print(min_boxes(k, boxes))
        test_cases -= 1


__starting_point()
