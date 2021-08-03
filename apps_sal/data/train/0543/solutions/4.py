for i in range(int(input())):
    trn = int(input())
    tr = input().split(" ")
    drn = int(input())
    dr = input().split(" ")
    tsn = int(input())
    ts = input().split(" ")
    dsn = int(input())
    ds = input().split(" ")
    for j in ts:
        if j not in tr:
            print("no")
            break
    else:
        for k in ds:
            if k not in dr:
                print("no")
                break
        else:
            print("yes")
