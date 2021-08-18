t = int(input())

for _ in range(t):
    n, z1, z2 = list(map(int, input().split()))

    arr = list(map(int, input().split()))

    for i in range(n):
        arr[i] = abs(arr[i])

    if (abs(z1) in arr) or (abs(z2) in arr):
        print(1)
        continue

    if (z1 == 0) or (z2 == 0):
        print(2)
        continue

    poss = True
    for i in arr:
        if ((abs(z1 + i) in arr) or (abs(z2 + i) in arr)) and \
                ((abs(z1 - i) in arr) or (abs(z2 - i) in arr)):
            pass
        else:
            poss = False
            break

    if poss:
        print(2)
        continue

    print(0)
