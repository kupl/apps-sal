for t in range(int(input().strip())):
    n = int(input().strip())
    x = int(input().strip())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    day = 1
    acc = 0
    isPossible = True
    for a in arr:
        acc += 1
        if acc > x:
            day += 1
            acc = 1
        if day >= a:
            isPossible = False
            break
    print('Possible' if isPossible else 'Impossible')
