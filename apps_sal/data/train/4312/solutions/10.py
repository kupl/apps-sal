
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    elif x == 0:
        return 0


def pick_peaks(arr):
    pos = []
    peaks = []
    l = len(arr)
    diff_arr = []
    for i in range(0, l - 1):
        diff_arr.append(sign(arr[i + 1] - arr[i]))
    i = 0
    while i < l - 2:
        k = 1
        while sign(diff_arr[i + k]) == 0 and i + k < l - 2:
            k += 1
        if (sign(diff_arr[i + k]) < sign(diff_arr[i])
                and sign(diff_arr[i]) != 0 and sign(diff_arr[i + k]) != 0):
            pos.append(i + 1)
            peaks.append(arr[i + 1])
        i += k
    d_pos_peaks = dict(pos=pos, peaks=peaks)
    return d_pos_peaks
