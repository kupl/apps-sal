for _ in range(int(input())):
    n = int(input())
    ings = list(map(int, input().split()))
    di_ings = {}
    last = 0
    possible = True
    for ing in ings:
        if ing in di_ings:
            if last == ing:
                di_ings[ing] += 1
            else:
                possible = False
                break
        else:
            di_ings[ing] = 1
            last = ing
    if possible and len(set(di_ings)) == len(set(di_ings.values())):
        print('YES')
    else:
        print('NO')
