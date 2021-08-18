for i in range(int(input())):
    Tr = int(input())
    Tr = list(map(int, input().split()))
    Dr = int(input())
    Dr = list(map(int, input().split()))
    Ts = int(input())
    Ts = list(map(int, input().split()))
    Ds = int(input())
    Ds = list(map(int, input().split()))
    for i in Ts:
        if i not in Tr:
            print("no")
            break
    else:
        for j in Ds:
            if j not in Dr:
                print("no")
                break
        else:
            print("yes")
