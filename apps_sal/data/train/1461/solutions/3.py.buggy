R1_HIGH, R1_LOW, R2_HIGH, R2_LOW = 0, 0, 0, 0


def cross_multiply(a, b, i):

    nonlocal R1_HIGH
    nonlocal R1_LOW
    nonlocal R2_HIGH
    nonlocal R2_LOW

    if i == 1:
        R1_HIGH = 6 * a * b
        R1_LOW = R1_HIGH // 2
    elif i == 2:
        R2_HIGH = 6 * a * b
        R2_LOW = R2_HIGH // 2


def isLess(a, b, c, d):
    cross_multiply(a, d, 1)
    cross_multiply(c, b, 2)

    if (R1_HIGH < R2_HIGH):
        return True

    if (R1_HIGH > R2_HIGH):
        return False

    return (R1_LOW < R2_LOW)


def negb_frac(a, b, N):
    leftN, leftD = 0, 1
    rightN, rightD = 1, 1

    while((leftD + rightD) <= N):
        mediantN = leftN + rightN
        mediantD = leftD + rightD

        if isLess(mediantN, mediantD, a, b):
            leftN = mediantN
            leftD = mediantD
        else:
            rightN = mediantN
            rightD = mediantD

            if (rightN == a and rightD == b):
                break

    if ((leftD + rightD) <= N):
        diff = N - (leftD + rightD)
        repeat = 1 + diff // rightD
        leftN += repeat * rightN
        leftD += repeat * rightD

    print(leftN, leftD)


def __starting_point():
    T = int(input())
    for _ in range(T):
        a, b, N = list(map(int, input().split()))
        negb_frac(a, b, N)


__starting_point()
