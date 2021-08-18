def read():
    return int(input())


def reads():
    return [int(x) for x in input().split()]


N = read()
A = reads()
B = reads()

D = 28
xor = 0
for d in range(D + 1):
    mask = (1 << (d + 1)) - 1
    AA = sorted(x & mask for x in A)
    BB = sorted(x & mask for x in B)
    count = 0
    itr = [N] * 4
    for a in AA:
        vs = [
            (1 << d) - a,
            (1 << (d + 1)) - a,
            (1 << d) + (1 << (d + 1)) - a,
            (1 << (d + 2)) - a
        ]
        for i in range(4):
            while 0 < itr[i] and vs[i] <= BB[itr[i] - 1]:
                itr[i] -= 1
        count += (itr[1] - itr[0]) + (itr[3] - itr[2])
    if count & 1:
        xor |= 1 << d

print(xor)
