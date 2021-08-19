(d1, v1, d2, v2, p) = list(map(int, input().split()))
if d1 == d2:
    check = 0
    start = d1 - 1
    v0 = v1 + v2
    if p % v0 == 0:
        print(p // v0 + start)
    else:
        print(p // v0 + 1 + start)
elif d2 < d1:
    con = d2
    pon = d1
    von = v2
else:
    con = d1
    pon = d2
    von = v1
if check != 0:
    starting_day = con - 1
    second = pon - con
    third = second * von
    if third > p:
        print(p // von + 1 + starting_day)
    elif third == p:
        print(second + starting_day)
    else:
        print((p - third) // (v2 + v1) + second + starting_day)
