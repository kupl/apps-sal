import sys


def main():
    t = int(input())
    while(t > 0):
        size = input()
        n = input().split()
        nmin = int(n[0])
        ndiff = 0
        for i in range(1, len(n)):
            k = int(n[i])
            if k < nmin:
                nmin = k
            else:
                if (k - nmin) > ndiff:
                    ndiff = k - nmin
        if ndiff > 0:
            print(ndiff)
        else:
            print("UNFIT")
        t -= 1


def __starting_point():
    main()
    return


__starting_point()
