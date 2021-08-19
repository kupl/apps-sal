# cook your dish here
def f(arr: list):
    arr.sort()
    # print(arr)
    pl, pr, pc = float('-inf'), float('-inf'), 0
    col = [0 for x in range(len(arr))]
    for i in arr:
        nl, nr = i[0], i[1]
        if nl > pr:
            i.append(0)
            pl, pr, pc = nl, nr, 0
        else:
            nc = 0 if pc == 1 else 1
            i.append(nc)
            pc = nc if nr > pr else pc
            pr = max(pr, nr)
        col[i[2]] = str(i[3])
    return "".join(col)


T = int(input())
for t in range(T):
    n = int(input())
    arr = []
    for i in range(n):
        l, r = [int(x) for x in input().split()]
        arr.append([l, r, i])
    print(f(arr))
