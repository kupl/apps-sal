def pick_peaks(array):
    peaks, pos = [], []
    platpos = platpeaks = ""

    for i in range(1, len(array) - 1):
        if array[i - 1] < array[i] > array[i + 1]:
            peaks.append(array[i]), pos.append(i)
        elif array[i - 1] < array[i] == array[i + 1]:
            platpos, platpeaks = i, array[i]
        elif array[i - 1] == array[i] > array[i + 1] and platpos != "":
            pos.append(platpos), peaks.append(platpeaks)

    return{"pos": pos, "peaks": peaks}
