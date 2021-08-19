def pick_peaks(arr):
    pos = []
    peaks = []
    n = 0

    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            pos.append(i)
            peaks.append(arr[i])

        # checking plateau cases
        elif arr[i] > arr[i - 1] and arr[i] == arr[i + 1]:
            n = 0
            for j in range(i + 1, len(arr)):
                # for the values that come after the possible plateau value
                # check to see that it decreases after staying constant

                if arr[j] == arr[i]:
                    n += 1

                else:
                    break

            if i + n + 1 < len(arr) and arr[i + n + 1] < arr[i]:

                pos.append(i)
                peaks.append(arr[i])

    return {"pos": pos, "peaks": peaks}
