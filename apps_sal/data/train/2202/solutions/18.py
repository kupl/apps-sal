

def sum_number(n, j):
    j[0] = 0
    j[1] = 0
    for i in range(2, n + 1):
        j[i] = j[i - 1] + (i - 1)
    return(j)


po = int(input())
l = [0] * (po + 1)
l1 = [int(i) for i in input().split()]


def getsum(BITTree, i):
    s = 0
    while i > 0:
        s += BITTree[i]
        i -= i & (-i)
    return(s)


def updatebit(BITTree, n, i, v):
    # print('n',n)
    while i <= n:
        # print('i',i)
        BITTree[i] += v
        i += i & (-i)

    # print(BITTree)
for i in range(1, po + 1):
    updatebit(l, po, i, i)
output = [0] * po
for i in range(po - 1, -1, -1):
    min_ = 0
    max_ = po
    k = l1[i]
    while True:
        x = (min_ + max_ + 1) // 2
        if getsum(l, x) > k:
            if getsum(l, x - 1) == k:
                output[i] = x
                break
            else:
                # print(x)
                max_ = x
        else:
            # print(x)
            min_ = x
    updatebit(l, po, x, -x)
print(*output)
