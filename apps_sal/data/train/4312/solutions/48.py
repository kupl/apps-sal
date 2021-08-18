def pick_peaks(arr):
    local_peaks = {
        'pos': [],
        'peaks': []
    }
    count = 1
    length = len(arr)
    while count < length - 1:

        value = arr[count]
        add_node = False
        if value >= arr[count + 1] and value > arr[count - 1]:
            if value == arr[count + 1]:
                for i in range(2, length - count):
                    if arr[count + i] > value:
                        break
                    elif arr[count + i] < value:
                        add_node = True

            else:
                add_node = True

        if add_node:
            local_peaks['pos'].append(count)
            local_peaks['peaks'].append(value)
        count += 1

    return local_peaks
