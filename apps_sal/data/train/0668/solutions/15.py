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
        if n == 0:
            print(0)
            continue
        if k == 0:
            print(0)
            continue

        a = list(map(int, input().split()))
        print(msumfinder(a, n, k))


programrun(tcases)
