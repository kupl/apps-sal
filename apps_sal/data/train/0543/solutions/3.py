# cook your dish here

for i in range(int(input())):
    _ = int(input())
    Tr = list(map(int, input().split()))
    _ = int(input())
    Dr = list(map(int, input().split()))
    _ = int(input())
    Ts = list(map(int, input().split()))
    _ = int(input())
    Ds = list(map(int, input().split()))

    for j in Ts:
        if j not in Tr:
            print("no")
            break
    else:
        for k in Ds:
            if k not in Dr:
                print("no")
                break
        else:
            print("yes")
