for _ in range(int(input())):
    (n, val) = (int(input()), list(map(int, input().split())))
    total_ct = 0
    counts = []
    for i in range(1, 9):
        counts.append(val.count(i))
    total_ct = min(counts)
    print(total_ct)
