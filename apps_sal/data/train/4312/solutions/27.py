def next_different_value(arr, index):
    next_index = index + 1
    while arr[index] == arr[next_index] and next_index != len(arr) - 1:
        next_index += 1
    return arr[index] > arr[next_index]

def pick_peaks(arr):
    res = {'pos': [], 'peaks': []}
    if len(arr) < 3:
        return res
    def fill_res(pos, peaks):
        res['pos'].append(pos)
        res['peaks'].append(peaks)
    for index, value in enumerate(arr):
        if index not in [0, len(arr) - 1]:
            if arr[index] > arr[index - 1] and next_different_value(arr, index):
                fill_res(index, value)
    return res
