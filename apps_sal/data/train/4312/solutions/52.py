def pick_peaks(arr):
    # your code here
    a_1 = []
    a_2 = []

    result_ab = {'pos': a_1, 'peaks': a_2}

    for i in range(0, (len(arr) - 1)):
        if (i != 0) and (i != len(arr) - 1):
            if (arr[i] > arr[i - 1]) and (arr[i] > arr[i + 1]):
                a_1.append(i)
                a_2.append(arr[i])
            elif (arr[i] > arr[i - 1]) and (arr[i] == arr[i + 1]):
                # elem = i
                copy_arr = arr[:]
                while (copy_arr[i] == copy_arr[i + 1]):
                    del copy_arr[i + 1]
                    if i != len(copy_arr) - 1:
                        if (copy_arr[i] > copy_arr[i + 1]):  # !!!
                            a_1.append(i)
                            a_2.append(arr[i])
                            break
                        elif (copy_arr[i] == copy_arr[i + 1]):
                            continue
                        else:
                            break
                    else:
                        break
            else:
                pass
        else:
            pass

    return result_ab
