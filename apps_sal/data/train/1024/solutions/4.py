# cook your dish here
over = 0
missing = 0

for i in range(int(input())):
    s, n, k, r = list(map(int, input().split()))

    totalSlicesNeeded = k
    currNeeded = k
    for i in range(n - 1):
        currNeeded *= r
        totalSlicesNeeded += currNeeded

    if totalSlicesNeeded > s:
        missing += totalSlicesNeeded - s
        print(f"IMPOSSIBLE {totalSlicesNeeded - s}")
    else:
        over += s - totalSlicesNeeded
        print(f"POSSIBLE {s - totalSlicesNeeded}")
if over >= missing:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
