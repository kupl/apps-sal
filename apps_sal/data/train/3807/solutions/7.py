def countsort(arr, cntarr, cntdict):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        leftcount = cntarr[:mid]
        right = arr[mid:]
        rightcount = cntarr[mid:]

        countsort(left, leftcount, cntdict)
        countsort(right, rightcount, cntdict)

        i = 0
        j = 0
        k = 0
        while(i < len(left) and j < len(right)):
            if left[i] > right[j]:
                arr[k] = right[j]

                for n in range(i, len(left)):
                    temp = leftcount[n]
                    cntdict[temp] = cntdict[temp] + 1

                cntarr[k] = rightcount[j]
                j = j + 1
            else:
                arr[k] = left[i]
                cntarr[k] = leftcount[i]
                i = i + 1

            k = k + 1

        while i < len(left):
            arr[k] = left[i]
            cntarr[k] = leftcount[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            arr[k] = right[j]
            cntarr[k] = rightcount[j]
            j = j + 1
            k = k + 1


def smaller(arr):
    posarr = [i for i in range(len(arr))]

    cntdict = {i: 0 for i in range(len(arr))}

    countsort(arr, posarr, cntdict)

    soln = []
    for i in range(len(arr)):
        soln.append(cntdict[i])

    return soln
