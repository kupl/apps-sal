for _ in range(int(input())):
    (N, K) = list(map(int, input().split()))
    s = input()
    cap = 0
    small = 0
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            cap += 1
        else:
            small += 1
    if cap == small:
        if K >= small:
            print('both')
        elif K < small:
            print('none')
    elif small > cap:
        if K >= small:
            print('both')
        elif K < cap:
            print('none')
        else:
            print('chef')
    elif cap > small:
        if K >= cap:
            print('both')
        elif K < small:
            print('none')
        else:
            print('brother')
