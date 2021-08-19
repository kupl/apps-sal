# cook your dish here
# cook your dish here
def binarySearch(ar, l, r, x):
    if r >= l:
        mid = (l + r) // 2
        if ar[mid] == x:
            return mid
        elif ar[mid] > x:
            return binarySearch(ar, l, mid - 1, x)
        else:
            return binarySearch(ar, mid + 1, r, x)
    else:
        return -1


t = int(input())
for _ in range(t):
    r, c, q = list(map(int, input().split()))
    er = []
    ar = []
    coun = 0
    for i in range(q):
        er.append(input().split())
        ar.append((int(er[i][0])) * (c + 1) + int(er[i][1]))
    ar = sorted(ar)
    for i in range(q):
        l = 0
        r = q - 1
        x = ((ar[i] // (c + 1) + 1) * (c + 1) + (ar[i] % (c + 1)))
        if binarySearch(ar, l, r, x) == -1:
            coun += 1
        x = ((ar[i] // (c + 1) - 1) * (c + 1) + (ar[i] % (c + 1)))
        if binarySearch(ar, l, r, x) == -1:
            coun += 1
        x = ar[i] + 1
        if i < q - 1:
            if ar[i + 1] != x:
                coun += 1
        else:
            coun += 1
        x = ar[i] - 1
        if i > 0:
            if ar[i - 1] != x:
                coun += 1
        else:
            coun += 1
    print(coun)
