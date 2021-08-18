def mergeSort(arr, n):
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n - 1)


def _mergeSort(arr, temp_arr, left, right):

    inv_count = 0

    if left < right:

        mid = (left + right) // 2

        inv_count = _mergeSort(arr, temp_arr, left, mid)

        inv_count += _mergeSort(arr, temp_arr, mid + 1, right)

        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count


def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count


'''
def merge(arr,start,mid,end):
    p=start
    q=mid+1
    k=0
    inv = 0
    temp=[0]*len(arr)
    for i in range(start,end+1):
     if p>mid :
      temp[k]=arr[q]
      k+=1
      q+=1
     elif q>end:
      temp[k]=arr[p]
      k+=1
      p+=1
     elif arr[p]<=arr[q]:
      temp[k]=arr[p]
      p+=1
      k+=1
     else:
      temp[k]=arr[q]
      q+=1
      k+=1
      inv += (mid-p+1)
    for i in range(k):
     arr[start]=temp[i]
     start+=1
 
    return inv

def mergesort(arr,start,end):
    inv_count=0 
    if start<end:
     mid=(start+end)//2
     inv_count += mergesort(arr,start,mid)
     inv_count += mergesort(arr,mid+1,end)
     inv_count += merge(arr,start,mid,end)
    return inv_count

'''
for _ in range(int(input())):
    n, d = list(map(int, input().split()))
    p = list(map(int, input().split()))

    inv_count = 0
    m = {}
    sb = True
    for i in range(d):
        k = 0
        for j in range(i, n, d):
            m[k] = p[j]
            k += 1
        inv_count += mergeSort(m, k)

        k = 0
        for j in range(i, n, d):
            if not(m[k] == (j + 1)):
                sb = False
                break
            k += 1

    if sb:
        print(inv_count)
    else:
        print(-1)
