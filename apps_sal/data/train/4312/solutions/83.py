def pick_peaks(arr):
    pos = []
    peak = []
    peaking = False
    platu = None
    for (count, item) in enumerate(arr):
        try:
            if arr[count] < arr[count + 1]:
                peaking = True
                platu = None
            elif arr[count] == arr[count + 1] and peaking:
                platu = count
                peaking = False
            elif peaking:
                pos.append(count)
                peak.append(item)
                peaking = False
            elif platu and arr[count + 1] > arr[count]:
                platu = None
                peaking = True
            elif platu and arr[count + 1] < arr[count]:
                pos.append(platu)
                peak.append(arr[platu])
                platu = None
                peaking = False
            else:
                pass
        except IndexError:
            break
    return {'pos': pos, 'peaks': peak}
