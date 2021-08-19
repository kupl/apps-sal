for _ in range(int(input())):
    n = int(input())
    goes = []
    for _ in range(n):
        z = input().split()
        goes.append((int(z[1]), z[0]))
    goes.sort()
    res = 'Nobody wins.'
    last = goes[0][0] - 1
    win = False
    for (val, nm) in goes:
        if val == last:
            win = False
        else:
            if win:
                res = lastnm
                break
            win = True
            lastnm = nm
            last = val
    print(res)
