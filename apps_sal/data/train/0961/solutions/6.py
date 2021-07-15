def merge(A, aux, low, mid, high):
 
    k = i = low
    j = mid + 1
    inversionCount = 0
 
    # While there are elements in the left and right runs
    while i <= mid and j <= high:
        if A[i] <= A[j]:
            aux[k] = A[i]
            i = i + 1
        else:
            aux[k] = A[j]
            j = j + 1
            inversionCount += (mid - i + 1)  # NOTE
 
        k = k + 1
 
    # Copy remaining elements
    while i <= mid:
        aux[k] = A[i]
        k = k + 1
        i = i + 1
 
    # Don't need to copy second half
 
    # copy back to the original list to reflect sorted order
    for i in range(low, high + 1):
        A[i] = aux[i]
 
    return inversionCount
 
 
# Sort list [low..high] using auxiliary space aux
def mergeSort(A, aux, low, high):
 
    # Base case
    if high == low:  # if run size == 1
        return 0
 
    # find mid point
    mid = low + ((high - low) >> 1)
    inversionCount = 0
 
    # recursively split runs into two halves until run size == 1,
    # then merge them and return back up the call chain
 
    inversionCount += mergeSort(A, aux, low, mid)        # split / merge left half
    inversionCount += mergeSort(A, aux, mid + 1, high)   # split / merge right half
    inversionCount += merge(A, aux, low, mid, high)      # merge the two half runs
 
    return inversionCount
 
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    aux=l.copy()
    print(mergeSort(l,aux,0,len(l)-1))
