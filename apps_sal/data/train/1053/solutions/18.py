from sys import stdin, stdout


def findTransitionPoint(arr, n):
    lb = 0
    ub = n - 1
    while (lb <= ub):
        mid = (int)((lb + ub) / 2)
        if (arr[mid] == 0):
            lb = mid + 1
        elif (arr[mid] == 1):
            if (mid == 0 or
                    (mid > 0 and
                        arr[mid - 1] == 0)):
                return mid
            ub = mid - 1
    return -1


test = int(stdin.readline())
for _ in range(test):
    n = int(stdin.readline())
    arr = sorted(list(map(int, stdin.readline().split())))
    pp = findTransitionPoint(arr, n)
    print(pp)
