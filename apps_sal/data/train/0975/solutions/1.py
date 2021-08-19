t = int(input())
for _ in range(t):
    (xi, yi) = ([], [])
    (n, r, x, y) = list(map(int, input().split()))
    if x > 0:
        xi = list(map(int, input().split()))
    if y > 0:
        yi = list(map(int, input().split()))
    part_cheat = {}
    for i in range(max(x, y)):
        if x > i:
            if xi[i] not in part_cheat:
                part_cheat[xi[i]] = True
        if y > i:
            if yi[i] not in part_cheat:
                part_cheat[yi[i]] = True
    cheaters = len(part_cheat)
    total = n - cheaters
    print(min(total, r))
