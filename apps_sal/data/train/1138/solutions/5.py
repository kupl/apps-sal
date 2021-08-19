for i in range(eval(input())):
    n = eval(input())
    arr = list(map(int, input().split()))
    place = []
    steps = 0
    for i in range(1, n + 1):
        pos = arr[i - 1]
        if pos == 0:
            place.insert(0, i)
        else:
            ind = place.index(pos)
            lef = ind + 1
            rig = i - 1 - lef
            if rig == 0:
                place.append(i)
            else:
                steps += min(lef, rig)
                place.insert(ind + 1, i)
    print(steps)
