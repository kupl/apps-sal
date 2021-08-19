def calFirstFreeDay(r, k, count):
    if r - k < k:
        print(count + 2)
    else:
        calFirstFreeDay(r - k, k, count + 1)


T = int(input())
for i in range(0, T):
    list = input().split()
    n = int(list[0])
    k = int(list[1])
    pq = 0
    outputDone = False
    arr = input().split()
    for j in range(0, n):
        q = int(arr[j])
        if q + pq < k:
            print(j + 1)
            outputDone = True
            break
        else:
            pq = q + pq - k
    if not outputDone:
        calFirstFreeDay(pq, k, n)
