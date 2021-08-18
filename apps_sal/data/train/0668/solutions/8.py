import math
tcases = int(input())
myanswer = []


def programrun(tcases):
    if tcases == 0:
        print(0)
        return

    def msumfinder(array, n, k):
        msofar = -10000000
        mendnow = 0
        for i in range(n * k):
            mendnow += array[i % n]
            if mendnow > msofar:
                msofar = mendnow
            if mendnow < 0:
                mendnow = 0
        return msofar

    for _ in range(0, tcases):
        fline = input().split()
        fline = list(map(int, fline))
        k = fline[1]
        n = fline[0]
        a = [int(x) for x in input().split()]
        sa = sum(a)
        if sa >= 0:
            if k == 1 or k == 2:
                print(msumfinder(a, n, k))
            else:
                print(msumfinder(a, n, 2) + (k - 2) * sa)

        else:
            if k == 1:
                print(msumfinder(a, n, 1))
            else:
                print(msumfinder(a, n, 2))


programrun(tcases)
