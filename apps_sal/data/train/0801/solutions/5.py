def chef_cost(A, B, n):

    checksum = 0  # if count of number is even XOR = 0, else it will give a value

    mn1 = min(A)
    mn2 = min(B)

    mn = min(mn1, mn2)

    mpa = {}
    for i in range(n):

        checksum ^= A[i]

        if A[i] not in mpa:
            mpa[A[i]] = 1
        else:
            mpa[A[i]] += 1

    mpb = {}
    for i in range(n):

        checksum ^= B[i]

        if B[i] not in mpb:
            mpb[B[i]] = 1
        else:
            mpb[B[i]] += 1

#     print(mpa)
#     print(mpb)

    if (checksum):  # numbers with odd count can never be distributed
        return -1

    # removing common elements
    for i in mpa:
        if i in mpb:
            dx = min(mpa[i], mpb[i])

            mpa[i] -= dx
            mpb[i] -= dx

#     print(mpa)
#     print(mpb)

    a1 = []
    b1 = []

    for i in mpa:
        for j in range(mpa[i] // 2):
            a1.append(i)

    for i in mpb:
        for j in range(mpb[i] // 2):
            b1.append(i)

    a1.sort()
    b1.sort(reverse=True)

    cost = 0
    for i in range(len(a1)):
        cost += min(2 * mn, min(a1[i], b1[i]))

    return cost


t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    print(chef_cost(A, B, n))
