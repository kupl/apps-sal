def merge(A, aux, low, mid, high):
    k = i = low
    j = mid + 1
    inversionCount = 0
    while i <= mid and j <= high:
        if A[i] <= A[j]:
            aux[k] = A[i]
            i = i + 1
        else:
            aux[k] = A[j]
            j = j + 1
            inversionCount += mid - i + 1
        k = k + 1
    while i <= mid:
        aux[k] = A[i]
        k = k + 1
        i = i + 1
    for i in range(low, high + 1):
        A[i] = aux[i]
    return inversionCount


def mergeSort(A, aux, low, high):
    if high == low:
        return 0
    mid = low + (high - low >> 1)
    inversionCount = 0
    inversionCount += mergeSort(A, aux, low, mid)
    inversionCount += mergeSort(A, aux, mid + 1, high)
    inversionCount += merge(A, aux, low, mid, high)
    return inversionCount


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    aux = l.copy()
    print(mergeSort(l, aux, 0, len(l) - 1))
