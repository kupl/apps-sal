def wave_sort(a):
    pivot = 0
    while pivot < len(a):
        max_val = max(a[pivot:])
        max_val_index = a[pivot:].index(max_val)
        tmp = a[pivot]
        a[pivot] = max_val
        a[max_val_index + pivot] = tmp
        pivot += 1

        if pivot < len(a):
            min_val = min(a[pivot:])
            min_val_index = a[pivot:].index(min_val)
            tmp = a[pivot]
            a[pivot] = min_val
            a[min_val_index + pivot] = tmp
            pivot += 1
