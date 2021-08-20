for i in range(int(input())):
    (n, m, k) = map(int, input().split())
    a = []
    item = {}
    count = 0
    for j in range(k):
        (x, y) = map(int, input().split())
        ele = (x, y)
        item[ele] = 1
        a.append([x, y])
        count += 4
        if item.get((x - 1, y)) == 1:
            count -= 2
        if item.get((x, y + 1)) == 1:
            count -= 2
        if item.get((x, y - 1)) == 1:
            count -= 2
        if item.get((x + 1, y)) == 1:
            count -= 2
    print(count)
