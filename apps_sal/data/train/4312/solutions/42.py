def pick_peaks(arr):
    result = []
    resultIndex = []
    for element in range(len(arr)):
        if element > 0 and element != len(arr) - 1:
            if arr[element] > arr[element - 1] and arr[element] > arr[element + 1]:
                peak = arr[element]
                result.append(peak)
                resultIndex.append(element)
            elif arr[element] > arr[element - 1] and arr[element] == arr[element + 1]:
                curr = arr[element]
                currIndex = element
                for next in range(element + 1, len(arr) - 1):
                    if arr[next] > arr[next + 1]:
                        result.append(curr)
                        resultIndex.append(currIndex)
                        break
                    elif arr[next] == arr[next + 1]:
                        continue
                    else:
                        break
    return {'pos': resultIndex, 'peaks': result}
