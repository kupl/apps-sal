def pick_peaks(arr):
    results = {'pos': [], 'peaks': []}

    for i in range(1, len(arr) - 1):
        if is_peak(arr, i):
            results['pos'].append(i)
            results['peaks'].append(arr[i])

    return results


def get_direction(last, i):
    if i > last:
        return 1
    elif i == last:
        return 0
    else:
        return -1


def is_peak(arr, index):
    result = False
    cur_val = arr[index]

    if get_direction(cur_val, arr[index - 1]) < 0:
        for i in range(index, len(arr)):
            dir = get_direction(cur_val, arr[i])
            if dir < 0:
                result = True
                break
            elif dir > 0:
                result = False
                break

    return result
