for _ in range(int(input())):
    tr = int(input())
    Tr = list(map(int, input().split()))
    dr = int(input())
    Dr = list(map(int, input().split()))
    ts = int(input())
    Ts = list(map(int, input().split()))
    ds = int(input())
    Ds = list(map(int, input().split()))

    for truth_s in Ts:
        if truth_s in Tr:
            flag = 1
        else:
            flag = 0
            break
    if flag:
        for dare_s in Ds:
            if dare_s in Dr:
                flag = 1
            else:
                flag = 0
                break

    if flag:
        print('yes')
    else:
        print('no')
