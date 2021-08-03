for x in range(0, eval(input())):
    p = list(map(int, input().split()))
    a = p[2]
    b = p[3]
    c = p[4]
    ro = p[0]
    co = p[1]
    ar = ro * co
    if a == ar or b == ar or c == ar:
        print("No")
        continue
    if a % ro == 0:
        nr = ro
        nc = co - (a / ro)
        if b % nr == 0 and c % nr == 0 and (b / nr) + (c / nr) == nc:
            print("Yes")
            continue
        else:
            if b % nc == 0 and c % nc == 0 and (b / nc) + (c / nc) == nr:
                print("Yes")
                continue
    if b % ro == 0:
        nr = ro
        nc = co - (b / ro)
        if a % nr == 0 and c % nr == 0 and (a / nr) + (c / nr) == nc:
            print("Yes")
            continue
        else:
            if a % nc == 0 and c % nc == 0 and (a / nc) + (c / nc) == nr:
                print("Yes")
                continue
    if c % ro == 0:
        nr = ro
        nc = co - (c / ro)
        if b % nr == 0 and a % nr == 0 and (b / nr) + (a / nr) == nc:
            print("Yes")
            continue
        else:
            if b % nc == 0 and a % nc == 0 and (b / nc) + (a / nc) == nr:
                print("Yes")
                continue
    if a % co == 0:
        nr = ro - (a / co)
        nc = co
        if b % nr == 0 and c % nr == 0 and (b / nr) + (c / nr) == nc:
            print("Yes")
            continue
        else:
            if b % nc == 0 and c % nc == 0 and (b / nc) + (c / nc) == nr:
                print("Yes")
                continue
    if b % co == 0:
        nr = ro - (b / co)
        nc = co
        if a % nr == 0 and c % nr == 0 and (a / nr) + (c / nr) == nc:
            print("Yes")
            continue
        else:
            if a % nc == 0 and c % nc == 0 and (a / nc) + (c / nc) == nr:
                print("Yes")
                continue
    if c % co == 0:
        nr = ro - (c / co)
        nc = co
        if b % nr == 0 and a % nr == 0 and (b / nr) + (a / nr) == nc:
            print("Yes")
            continue
        else:
            if b % nc == 0 and a % nc == 0 and (b / nc) + (a / nc) == nr:
                print("Yes")
                continue
    print("No")
