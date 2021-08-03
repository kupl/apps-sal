t = int(input())
while t:
    n = int(input())
    l = list(map(int, input().split()))
    suma = 0
    c = 0
    index1 = -1
    for i in range(n):
        if l[i] != 0:
            index1 = i
            break
    index2 = -1
    for i in range(n - 1, -1, -1):
        if l[i] != 0:
            index2 = i
            break
    if index1 != -1 and index2 != -1:
        print(index2 - index1 + 1)
    else:
        print(1)

    t -= 1
