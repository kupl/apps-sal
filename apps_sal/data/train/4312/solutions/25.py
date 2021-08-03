def pick_peaks(arr):
    maximas, positions = [], []
    for i, num in enumerate(arr):
        same_as_num = [x == num for x in arr[i:]]
        end = not all(same_as_num) and i + same_as_num.index(False) - 1
        local_max = end and num > arr[i - 1] and num > arr[end + 1]

        if not (i == 0 or i == len(arr) - 1) and local_max:
            maximas.append(arr[i])
            positions.append(i)

    return {"pos": positions, "peaks": maximas}
