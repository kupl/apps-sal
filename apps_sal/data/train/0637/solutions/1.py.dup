import sys


def input():
    return sys.stdin.readline().strip()


for i in range(int(input())):
    n, k = map(int, input().split())
    arr = []
    if k == 2 or k == 4 or n % 2 != 0 or n == k:
        arr.append('-1')
    elif k % 2 != 0:
        for i in range(int(n / 2)):
            arr.append('(')
        for i in range(int(n / 2)):
            arr.append(')')
    elif int(n / (k - 2)) == 1:
        if (n - 2) % 4 == 0:
            for i in range(int((n - 2) / 4)):
                arr.append('(')
            for i in range(int((n - 2) / 4)):
                arr.append(')')
            arr.append('()')
            for i in range(int((n - 2) / 4)):
                arr.append('(')
            for i in range(int((n - 2) / 4)):
                arr.append(')')
        else:
            for i in range(int((n - 4) / 4)):
                arr.append('(')
            for i in range(int((n - 4) / 4)):
                arr.append(')')
            arr.append('(())')
            for i in range(int((n - 4) / 4)):
                arr.append('(')
            for i in range(int((n - 4) / 4)):
                arr.append(')')
    else:
        for i in range(int((n % (k - 2)) / 2)):
            arr.append('(')
        for i in range(int(n / (k - 2))):
            for j in range(int((k - 2) / 2)):
                arr.append('(')
            for j in range(int((k - 2) / 2)):
                arr.append(')')
        for i in range(int((n % (k - 2)) / 2)):
            arr.append(')')

    print("".join(arr))
