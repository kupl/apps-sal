def pick_peaks(arr):
    output = {"pos": [], "peaks": []}
    topPos = 0
    if len(arr) > 0:
        topPeak = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                topPos = i
                topPeak = arr[i]
            elif arr[i] < arr[i - 1]:
                """ It's help to know if there was a climbing previously """
                if topPos > 0:
                    output["pos"].append(topPos)
                    output["peaks"].append(topPeak)
                    topPos = 0
    return output
