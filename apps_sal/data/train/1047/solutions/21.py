import bisect


def sign(a):
    if(a == abs(a)):
        return 1
    else:
        return -1


def insert(list, n):
    bisect.insort(list, n)
    return list


t = int(input())
for i in range(0, t):
    n = int(input())

    arr = []
    brr = []
    for j in range(0, n):
        x, y = input().split()
        x = int(x)
        y = int(y)
        a = x - y
        b = x + y
        insert(arr, a)
        insert(brr, b)
    m1 = arr[1] - arr[0]
    for k in range(1, len(arr) - 1):
        if((arr[k + 1] - arr[k]) < m1):
            m1 = arr[k + 1] - arr[k]
    m2 = brr[1] - brr[0]
    for k in range(1, len(arr) - 1):
        if((brr[k + 1] - brr[k]) < m2):
            m2 = brr[k + 1] - brr[k]
    print((min(m1, m2)) / 2)
