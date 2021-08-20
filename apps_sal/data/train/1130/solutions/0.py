for _ in range(int(input())):
    (f, d) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    risk = 0
    days_risk = 0
    days_norm = 0
    if d == 1:
        print(f)
    else:
        for a in arr:
            if a >= 80 or a <= 9:
                risk += 1
        norm = f - risk
        if risk % d == 0:
            days_risk = risk // d
        else:
            days_risk = risk // d + 1
        if norm % d == 0:
            days_norm = norm // d
        else:
            days_norm = norm // d + 1
        print(days_risk + days_norm)
